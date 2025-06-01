import os
from datetime import datetime, timedelta
from django.conf import settings
from django.utils.text import get_valid_filename
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from azure.storage.blob import (
    BlobServiceClient,
    BlobSasPermissions,
    ContentSettings,
    generate_blob_sas,
)
from azure.core.exceptions import ResourceExistsError, ResourceNotFoundError

# Allowed MIME types
ALLOWED_CONTENT_TYPES = { "image/jpeg","image/png", "image/gif"}

def get_blob_service():
    return BlobServiceClient.from_connection_string(settings.AZURE_STORAGE_CONNECTION_STRING)


def get_or_create_container():
    blob_service = get_blob_service()
    container_client = blob_service.get_container_client(settings.AZURE_CONTAINER)
    
    try:
        container_client.get_container_properties()
    except ResourceNotFoundError:
        try:
            container_client.create_container()
        except ResourceExistsError:
            pass  # Already exists (race condition-safe)
    
    return container_client, blob_service

class AzureImageUploadView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = []  # Add IsAuthenticated if auth is required

    def post(self, request, *args, **kwargs):
        uploaded_files = request.FILES.getlist("files")
        if not uploaded_files:
            return Response({"detail": "No files uploaded."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            container_client, blob_service = get_or_create_container()
        except Exception as e:
            return Response({"detail": f"Azure connection error: {str(e)}"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        uploaded_urls = []

        for file in uploaded_files:
            
            # Validate MIME type
            if file.content_type not in ALLOWED_CONTENT_TYPES:
                return Response(
                    {"detail": f"File type not allowed: {file.content_type}"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Clean and secure the original filename
            safe_filename = get_valid_filename(os.path.basename(file.name))
            blob_path = f"media/image_question/{safe_filename}"

            try:
                blob = container_client.get_blob_client(blob_path)
                blob.upload_blob(
                    data=file,
                    overwrite=True,
                    content_settings=ContentSettings(content_type=file.content_type),
                )

                # Generate public or SAS-protected URL
                if getattr(settings, "AZURE_CONTAINER_IS_PUBLIC", False):
                    uploaded_urls.append(blob.url)
                else:
                    sas_token = generate_blob_sas(
                        account_name=blob_service.account_name,
                        container_name=settings.AZURE_CONTAINER,
                        blob_name=blob_path,
                        account_key=blob_service.credential.account_key,
                        permission=BlobSasPermissions(read=True),
                        expiry=datetime.utcnow() + timedelta(hours=12),
                    )
                    uploaded_urls.append(f"{blob.url}?{sas_token}")

            except Exception as e:
                return Response(
                    {"detail": f"Upload failed for {file.name}: {str(e)}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

        return Response({"files": uploaded_urls}, status=status.HTTP_201_CREATED)
