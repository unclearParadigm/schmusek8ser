from config import Config
from k8sbusinesslogic.k8s_session import K8sSession
from notificationsinks.notification_sinks import NotificationSinks

config = Config()
k8s = K8sSession(config)
notification_sinks = NotificationSinks(config)