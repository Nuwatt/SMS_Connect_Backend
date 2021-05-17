from apps.response.usecases import GetResponseUseCase


class ResponseMixin:
    def get_response(self, *args, **kwargs):
        return GetResponseUseCase(
            response_id=self.kwargs.get('response_id')
        ).execute()
