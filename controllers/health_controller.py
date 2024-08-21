from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse
from k8sbusinesslogic.k8s_session import K8sSession
from controllers._base_controller import BaseController


class HealthController(BaseController):
    k8s_session: K8sSession

    def __init__(self, k8s_session: K8sSession) -> None:
        self.k8s_session = k8s_session


    def handle(self, _: ApiRequest) -> ApiResponse:
        if not self.k8s_session.is_connected():
            return ApiResponse(500, success=False, error='Kubernetes API not reachable, or unauthenticated')

        return ApiResponse(200, success=True)

    @staticmethod
    def get_supported_methods() -> list:
        return ['GET']
