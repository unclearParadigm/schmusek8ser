import json
import base64
import binascii
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

import static
import utils.log as log

from models.apikey import ApiKey
from models.apirequest import ApiRequest
from models.apiresponse import ApiResponse

from controllers.bump_controller import BumpController
from controllers.index_controller import IndexController
from controllers.health_controller import HealthController
from controllers.apikey_controller import ApiKeyController
from controllers.restart_controller import RestartController
from middleware.requires_auth_middleware import RequiresApiKeyAuthMiddleware


# noinspection PyPep8Naming
class Router(BaseHTTPRequestHandler):
    route_dict = {
        '/': IndexController(),
        '/health': HealthController(static.k8s),
        '/bump': RequiresApiKeyAuthMiddleware(BumpController(static.k8s), static.config.AUTHORIZED_API_KEYS),
        '/restart': RequiresApiKeyAuthMiddleware(RestartController(static.k8s), static.config.AUTHORIZED_API_KEYS),
        '/apikey/new': ApiKeyController()
    }

    def do_GET(self):
        self._convert_api_response(self._handle_generic())

    def do_POST(self):
        self._convert_api_response(self._handle_generic())

    def do_PUT(self):
        self._convert_api_response(self._handle_generic())

    def do_DELETE(self):
        self._convert_api_response(self._handle_generic())

    def log_message(self, format, *args):
        pass

    def _convert_api_response(self, data: tuple) -> None:
        req, res = data
        self.send_response(res.status_code)
        self.send_header('charset', 'utf-8')
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps(res.__dict__, indent=2), 'utf8'))
        log.info(f'Request \'{req.trace_id}\' for route \'{req.request_url}\' finished with status {res.status_code}')

    def _handle_generic(self) -> (ApiRequest, ApiResponse):
        parsed_path = str(urlparse(self.path).path)
        if parsed_path == '':
            parsed_path = '/'
        query_params = parse_qs(urlparse(self.path).query)
        auth_api_key = self.try_parse_api_key()

        api_request = ApiRequest(parsed_path, self.command, auth_api_key, query_params, self.try_parse_http_payload())
        log.info(f'Request \'{api_request.trace_id}\' received for route \'{parsed_path}\'')
        route_matches = [controller for route, controller in self.route_dict.items() if route.startswith(parsed_path)]

        if len(route_matches) == 0:
            return (api_request,
                    ApiResponse(404, success=False, error='Requested resource not found.'))
        if len(route_matches) > 1:
            return (api_request,
                    ApiResponse(500, success=False, error='Ambiguous route matching multiple controllers.'))
        if self.command not in route_matches[0].get_supported_methods():
            return (api_request,
                    ApiResponse(405, success=False, error=f'Method {self.command} not allowed for route.'))

        # noinspection PyBroadException
        try:
            response = route_matches[0].handle(api_request)
            if response is None:
                return (api_request,
                        ApiResponse(500, success=False, error='Endpoint not yet implemented'))
            return api_request, response
        except Exception as _:
            return (
                api_request,
                ApiResponse(500, success=False, error='Internal Server Error while handling request')
            )

    def try_parse_api_key(self) -> ApiKey | None:
        try:
            api_key_b64_encoded = self.headers.get('X-API-KEY', None)
            if api_key_b64_encoded is None:
                return None
            api_key_object_text = base64.b64decode(api_key_b64_encoded, validate=True)
            api_key_object_dict = dict(json.loads(api_key_object_text))
            api_key_desc = api_key_object_dict.get('whose', None)
            api_key_token = api_key_object_dict.get('token', None)
            if api_key_token is None:
                return None
            return ApiKey(api_key_token, api_key_desc)
        except binascii.Error as _:
            return None
        except json.JSONDecodeError as _:
            return None
        except TypeError as _:
            return None
        except ValueError as _:
            return None

    def try_parse_http_payload(self) -> dict | None:
        try:
            content_length = int(self.headers['Content-Length'])
            if content_length == 0:
                return None

            payload_as_text = self.rfile.read(content_length)
            payload_as_dict = json.loads(payload_as_text)
            return payload_as_dict
        except json.JSONDecodeError as _:
            return None
        except TypeError as _:
            return None
        except ValueError as _:
            return None
