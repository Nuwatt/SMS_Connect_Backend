# apps/core/azure_storage.py
import os
from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = os.environ.get('AZURE_ACCOUNT_NAME', 'stsmsproduaenmerchandise')
    account_key = os.environ.get('AZURE_ACCOUNT_KEY', '')
    azure_container = os.environ.get('AZURE_CONTAINER', 'smsmerchandise-media')
    expiration_secs = None
    custom_domain = os.environ.get('AZURE_CUSTOM_DOMAIN', 'stsmsproduaenmerchandise.blob.core.windows.net')

class AzureStaticStorage(AzureStorage):
    account_name = os.environ.get('AZURE_ACCOUNT_NAME', 'stsmsproduaenmerchandise')
    account_key = os.environ.get('AZURE_ACCOUNT_KEY', '')
    azure_container = os.environ.get('AZURE_STATIC_CONTAINER', 'static')
    expiration_secs = None
    custom_domain = os.environ.get('AZURE_CUSTOM_DOMAIN', 'stsmsproduaenmerchandise.blob.core.windows.net')

class AzurePrivateMediaStorage(AzureStorage):
    account_name = os.environ.get('AZURE_ACCOUNT_NAME', 'stsmsproduaenmerchandise')
    account_key = os.environ.get('AZURE_ACCOUNT_KEY', '')
    azure_container = os.environ.get('AZURE_PRIVATE_CONTAINER', 'private')
    expiration_secs = None
    custom_domain = os.environ.get('AZURE_CUSTOM_DOMAIN', 'stsmsproduaenmerchandise.blob.core.windows.net')