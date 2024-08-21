from config import Config
from notificationsinks.base_sink import BaseSink
from notificationsinks.ntfy import Ntfy


class NotificationSinks(BaseSink):
    config: Config

    def __init__(self, config: Config):
        self.config = config

        self.sinks = [
            Ntfy(self.config)
        ]

    def post(self, title: str, message: str) -> None:
        for sink in self.sinks:
            sink.post(title, message)