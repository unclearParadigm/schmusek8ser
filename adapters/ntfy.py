import requests
from urllib.parse import urljoin

from config import Config


class Ntfy(object):
    def __init__(self, config: Config):
        self.config = config

    def post(self, title: str, message: str):
        if not self.config.NTFY_ENABLE:
            return

        ntfy_url = urljoin(self.config.NTFY_BASE_URL, self.config.NTFY_TOPIC)
        requests.post(ntfy_url, data=message, headers={'Title': title, 'Tags': 'smiley_cat'})
