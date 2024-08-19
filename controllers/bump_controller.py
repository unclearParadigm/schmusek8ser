from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse
from k8sbusinesslogic.k8s_session import K8sSession


class BumpController(object):
    def __init__(self, k8s_session: K8sSession):
        self.k8s_session = k8s_session

    def handle(self, request: ApiRequest) -> ApiResponse:
        return ApiResponse(500, success=False, error='Not yet implemented.')

    @staticmethod
    def get_supported_methods() -> list:
        return ['POST']
