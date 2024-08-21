import requests
from urllib.parse import urljoin

from requests import HTTPError, Timeout, TooManyRedirects

from notificationsinks.base_sink import BaseSink
from utils import log
from config import Config


class Ntfy(BaseSink):
    config: Config

    def __init__(self, config: Config) -> None:
        self.config = config

    def post(self, title: str, message: str) -> None:
        if not self.config.NTFY_ENABLE:
            return

        try:
            ntfy_url = urljoin(self.config.NTFY_BASE_URL, self.config.NTFY_TOPIC)
            requests.post(ntfy_url, data=message, headers={'Title': title, 'Tags': 'smiley_cat'})
        except ConnectionError:
            log.error(f'Cannot connect to {self.config.NTFY_BASE_URL}. DNS request or TCP 3-way handshake failed')
        except HTTPError:
            log.error(f'Received Malformed HTTP response from {self.config.NTFY_BASE_URL}')
        except Timeout:
            log.error(f'Ran into an Timeout while sending Notification to {self.config.NTFY_BASE_URL}')
        except TooManyRedirects:
            log.error(f'Got redirected to often while sending notifications to {self.config.NTFY_BASE_URL}')


