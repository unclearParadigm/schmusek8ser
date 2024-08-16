import uuid

from models.apikey import ApiKey


class ApiRequest(object):
    def __init__(self,
                 request_url: str,
                 method: str,
                 api_key: ApiKey | None,
                 query_params: dict | None,
                 payload: dict | None):
        self.request_url = str(request_url)
        self.method = str(method)
        self.api_key = api_key
        self.query_params = dict(query_params) if query_params is not None else None
        self.payload = dict(payload) if payload is not None else None
        self.trace_id = str(uuid.uuid4())

