import datetime

from kubernetes import client, config
from kubernetes.client import ApiException

import utils.log as log
from config import Config
from k8sbusinesslogic.k8s_operation_result import K8sOperationResult


class K8sSession(object):
    def __init__(self, cfg: Config):
        try:
            log.info(f'Loading K8s config from \'{cfg.K8S_KUBECONFIG_PATH}\' with CTX \'{cfg.K8S_KUBECONFIG_CTX}\'')
            config.load_kube_config(
                config_file=cfg.K8S_KUBECONFIG_PATH,
                context=cfg.K8S_KUBECONFIG_CTX,
                persist_config=False)
        except Exception as e:
            log.error(f'Could not load/read K8s Configuration from the specified path \'{cfg.K8S_KUBECONFIG_PATH}\'')
            exit(1)

        try:
            log.info(f'Initializing K8s API Client')
            self.v1_apps = client.AppsV1Api()
        except Exception as e:
            log.error(f'Failed to Load AppsV1 API ')
            exit(1)


    def is_connected(self) -> K8sOperationResult:
        try:
            self.v1_apps.get_api_resources()
            return K8sOperationResult('is_connected', success=True)
        except:
            return K8sOperationResult('is_connected', success=False, error='Failed to query API resources.')


    def bump_deployment(self, deployment: str, namespace: str, target_tag: str, container: str,
                        who: str) -> K8sOperationResult:

        tag_before = ""

        now = str(datetime.datetime.now(datetime.UTC).isoformat("T") + "Z")
        body = {
            'spec': {
                'template': {
                    'metadata': {
                        'annotations': {
                            'schmusek8ser.bump/who': who,
                            'schmusek8ser.bump/when': now,
                            'schmusek8ser.bump/tag/before': tag_before,
                            'schmusek8ser.bump/tag/after': target_tag,
                            'kubectl.kubernetes.io/restartedAt': now,
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


    def restart_deployment(self, deployment: str, namespace: str, who: str) -> K8sOperationResult:
        now = str(datetime.datetime.now(datetime.UTC).isoformat("T") + "Z")
        body = {
            'spec': {
                'template': {
                    'metadata': {
                        'annotations': {
                            'schmusek8ser.restart/who': who,
                            'schmusek8ser.restart/when': now,
                            'kubectl.kubernetes.io/restartedAt': now
                        }
                    }
                }
            }
        }
        try:
            self.v1_apps.patch_namespaced_deployment(deployment, namespace, body, pretty='true')
            return K8sOperationResult('restart_deployment', success=True, error=None)
        except ApiException as e:
            return K8sOperationResult('restart_deployment', success=True, error=str(e))
