import uuid
import string
import secrets

from models.apikey import ApiKey
from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse
from controllers._base_controller import BaseController


class ApiKeyController(BaseController):
    def handle(self, api_request: ApiRequest) -> ApiResponse:
        for_api_key_param = api_request.query_params.get('for')
        if for_api_key_param is None:
            return ApiResponse(400, success=False, error='URL query parameter \'?for\' missing')

        return ApiResponse(200, success=True, payload={
            'apiKey': str(ApiKey(token=self._generate_token(), whose=str(list(for_api_key_param)[0]))),
            'for': str(list(for_api_key_param)[0]),
            'note': 'This API key is not yet activated. Update the schmusek8ser configuration with this key'
        })

    @staticmethod
    def get_supported_methods() -> list:
        return ['GET']

    @staticmethod
    def _generate_token() -> str:
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        return f"{''.join(secrets.choice(letters) for i in range(32))}-{str(uuid.uuid4())}"
