import utils.log as log
from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse


class RequiresApiKeyAuthMiddleware(object):
    def __init__(self, controller, allowed_api_keys: list) -> None:
        self.controller = controller
        self.allowed_api_keys = list(allowed_api_keys)

    def get_supported_methods(self) -> list:
        return self.controller.get_supported_methods()

    def handle(self, api_request: ApiRequest) -> ApiResponse:
        if api_request.api_key is None or str(api_request.api_key) not in self.allowed_api_keys:
            log.warning(f'Request \'{api_request.trace_id}\' is not authenticated/authorized. Aborting.')
            return ApiResponse(401, success=False, error='Unauthenticated/Unauthorized request.')

        log.info(f'Request \'{api_request.trace_id}\' authenticated by API Key {api_request.api_key.get_masked()}')
        return self.controller.handle(api_request)
