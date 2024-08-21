import static
import utils.log as log
from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse
from k8sbusinesslogic.k8s_session import K8sSession
from controllers._base_controller import BaseController

class RestartController(BaseController):
    k8s_session: K8sSession

    def __init__(self, k8s_session: K8sSession):
        self.k8s_session = k8s_session

    def handle(self, request: ApiRequest) -> ApiResponse:
        namespace_query_param = request.query_params.get('namespace')
        if namespace_query_param is None:
            return ApiResponse(400, success=False, error='URL query parameter \'?namespace\' missing')
        deployment_query_param = request.query_params.get('deployment')
        if deployment_query_param is None:
            return ApiResponse(400, success=False, error='URL query parameter \'?deployment\' missing')

        namespace = list(namespace_query_param)[0]
        deployment = list(deployment_query_param)[0]

        res = self.k8s_session.restart_deployment(deployment, namespace, request.api_key.who)
        if res.success:
            log.info(f'Successfully triggered restart of deployment \'{deployment}\ in namespace \'{namespace}\'')
            title = f'[restart] {namespace}/{deployment}'
            message = f'Successfully restarted {namespace}/{deployment}. Initiated by \'{request.api_key.who}\''
            static.notification_sinks.post(title, message)
            return ApiResponse(201, success=True)
        else:
            log.warning(f'Failed restart of \'{deployment}\ in namespace \'{namespace}\' because \'{res.error}\'')
            title = f'[restart] {namespace}/{deployment}'
            message = f'Failed to restart {namespace}/{deployment}. Initiated by \'{request.api_key.who}\''
            static.notification_sinks.post(title, message)
            return ApiResponse(500, success=False, error='Namespace or Deployment by name does not exist.')


    @staticmethod
    def get_supported_methods() -> list:
        return ['POST']
