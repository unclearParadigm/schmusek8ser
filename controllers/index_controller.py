import version
from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse
from controllers._base_controller import BaseController

class IndexController(BaseController):
    def __init__(self) -> None:
        pass

    def handle(self, _: ApiRequest) -> ApiResponse:
        payload = {
            'service': 'schmusek8ser',
            'version': version.VERSION,
            'repository': 'https://github.com/unclearParadigm/schmusek8ser'
        }
        return ApiResponse(200, success=True, payload=payload)

    @staticmethod
    def get_supported_methods() -> list:
        return ['GET']
