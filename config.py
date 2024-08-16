from loguru import logger
from config_utils import list_env_var
from config_utils import env_var_or_default


class Config(object):
    # API CONFIG
    LISTEN_PORT = int(env_var_or_default('SCHMUSEK8SER_LISTEN_PORT', 8080))
    LISTEN_HOST = str(env_var_or_default('SCHMUSEK8SER_LISTEN_HOST', '0.0.0.0'))
    AUTHORIZED_API_KEYS = list(list_env_var('SCHMUSEK8SER_AUTHORIZED_API_KEYS'))

    # K8S CONFIG
    K8S_KUBECONFIG_PATH = str(env_var_or_default('SCHMUSEK8SER_K8S_KUBECONFIG_PATH', '/home/rare/.kube/config'))
    K8S_KUBECONFIG_CTX = env_var_or_default('SCHMUSEK8SER_K8S_KUBECONFIG_PATH', None)

    # NTFY CONFIG
    NTFY_ENABLE = bool(env_var_or_default('SCHMUSEK8SER_NTFY_ENABLE', False))
    NTFY_BASE_URL = str(env_var_or_default('SCHMUSEK8SER_NTFY_BASE_URL', 'https://ntfy.rtrace.io'))
    NTFY_TOPIC = str(env_var_or_default('SCHMUSEK8SER_NTFY_TOPIC', 'schmusek8ser'))

    def __init__(self):
        logger.info('Initialized Schmuserk8tser Configuration')





