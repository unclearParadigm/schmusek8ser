from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse


class HealthController(object):
    @staticmethod
    def handle(_: ApiRequest) -> ApiResponse:
        return ApiResponse(200, success=True)

    @staticmethod
    def get_supported_methods() -> list:
        return ['GET', 'POST']
