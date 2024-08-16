import base64
import json


class ApiKey(object):
    def __init__(self, token: str, whose: str) -> None:
        self.token = str(token)
        self.who = str(whose)
        self.api_key = self._create_api_key()

    def _create_api_key(self) -> str:
        serialized = json.dumps({'whose': self.who, 'token': self.token})
        return base64.b64encode(bytes(serialized, encoding='utf-8')).decode('utf-8')

    def __str__(self) -> str:
        return self._create_api_key()

    def get_masked(self) -> str:
        return self.api_key[:-80] + ('*'*16)
