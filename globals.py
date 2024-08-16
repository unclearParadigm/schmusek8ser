from config import Config
from adapters.ntfy import Ntfy
from k8sbusinesslogic.k8s_session import K8sSession

config = Config()
k8s = K8sSession(config)
ntfy = Ntfy(config)
