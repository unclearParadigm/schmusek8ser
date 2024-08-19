import static

from loguru import logger

from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse
from k8sbusinesslogic.k8s_session import K8sSession


class RestartController(object):
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
            logger.info(f'Successfully triggered restart of deployment \'{deployment}\ in namespace \'{namespace}\'')
            static.ntfy.post(f'{namespace}/{deployment} bumped', f'Successfully bumped {namespace}/{deployment} by \'{request.api_key.who}\'')
            return ApiResponse(201, success=True)
        else:
            logger.warning(f'Failed restart of \'{deployment}\ in namespace \'{namespace}\' because \'{res.error}\'')
            return ApiResponse(500, success=False, error='Failed to restart')


    @staticmethod
    def get_supported_methods() -> list:
        return ['POST']
