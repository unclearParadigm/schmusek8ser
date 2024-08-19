from os import environ
from loguru import logger
from config_utils import list_env_var




class Config(object):
    # API CONFIG
    LISTEN_PORT = int(environ.get('SCHMUSEK8SER_LISTEN_PORT', 8080))
    LISTEN_HOST = str(environ.get('SCHMUSEK8SER_LISTEN_HOST', '0.0.0.0'))
    AUTHORIZED_API_KEYS = list(list_env_var('SCHMUSEK8SER_AUTHORIZED_API_KEYS'))

    # K8S CONFIG
    K8S_KUBECONFIG_PATH = str(environ.get('SCHMUSEK8SER_K8S_KUBECONFIG_PATH', '/home/rare/.kube/config'))
    K8S_KUBECONFIG_CTX = environ.get('SCHMUSEK8SER_K8S_KUBECONFIG_CTX', None)

    # NTFY CONFIG
    NTFY_ENABLE = bool(environ.get('SCHMUSEK8SER_NTFY_ENABLE', False))
    NTFY_BASE_URL = str(environ.get('SCHMUSEK8SER_NTFY_BASE_URL', 'https://ntfy.rtrace.io'))
    NTFY_TOPIC = str(environ.get('SCHMUSEK8SER_NTFY_TOPIC', 'schmusek8ser'))

    def __init__(self):
        logger.info('Initialized Schmuserk8tser Configuration')





