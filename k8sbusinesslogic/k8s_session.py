import datetime

from loguru import logger
from kubernetes import client, config
from kubernetes.client import ApiException

from config import Config
from k8sbusinesslogic.k8s_operation_result import K8sOperationResult


class K8sSession(object):
    def __init__(self, cfg: Config):

        try:
            logger.info(f'Loading K8s config from \'{cfg.K8S_KUBECONFIG_PATH}\' with CTX \'{cfg.K8S_KUBECONFIG_CTX}\'')
            config.load_kube_config(
                config_file=cfg.K8S_KUBECONFIG_PATH,
                context=cfg.K8S_KUBECONFIG_CTX,
                persist_config=False)
        except Exception as e:
            logger.error(f'Could not load/read K8s Configuration from the specified path \'{cfg.K8S_KUBECONFIG_PATH}\'')
            exit(1)

        try:
            logger.info(f'Initializing K8s API Client')
            self.v1_apps = client.AppsV1Api()
        except Exception as e:
            logger.error(f'Failed to Load AppsV1 API ')
            exit(1)

    def restart_deployment(self, deployment, namespace, who) -> K8sOperationResult:
        now = datetime.datetime.now(datetime.UTC)
        now = str(now.isoformat("T") + "Z")
        body = {
            'spec': {
                'template': {
                    'metadata': {
                        'annotations': {
                            'kubectl.kubernetes.io/restartedAt': now,
                            'schmusek8ser.bump/who': who,
                            'schmusek8ser.bump/when': now
                        }
                    }
                }
            }
        }
        try:
            self.v1_apps.patch_namespaced_deployment(deployment, namespace, body, pretty='true')
            return K8sOperationResult('patch_namespaced_deployment', success=True, error=None)

        except ApiException as e:
            return K8sOperationResult('patch_namespaced_deployment', success=True, error=str(e))
