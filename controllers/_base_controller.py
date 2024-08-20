from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse


class BaseController(object):
    def handle(self, api_request: ApiRequest) -> ApiResponse:
        raise NotImplementedError()

    @staticmethod
    def get_supported_methods() -> list:
        raise NotImplementedError()