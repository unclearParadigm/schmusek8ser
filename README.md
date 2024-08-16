# schmusk8ser

schmusek8ser (pronounced 'schmusekadser') is a Python REST API able to connect to Kubernetes clusters and forcing pulls of `:latest` tags of deployments in a cluster.
This is particularily helpful for workloads which are mostly stateless and which you'd like to keep up to date with the latest tag automagically. No need to play around with [FluxCD](https://fluxcd.io),
and no need to expose your Kubernetes API to Source Code Repository hosters such as Gitlab/Github and the likes. Install `schmusk8ser` either as manifest in your K8s cluster, or run it on a machine
that can access the K8s API of your choice.

## Features

- [x] 🔑 authentication using simple and secure API Tokens
- [x] 🚀 easy to use REST-API
- [x] 🖹 audit logging
- [x] 📲 [ntfy.sh Notification dispatch support](https://ntfy.sh) for push notifications
- [x] 🔄 allow restarts of Deployments with `imagePullPolicy: always`
- [ ] 🐋 deployable as docker/podman container
- [ ] 🇰 K8s manifests available
- [ ] 👷 Helm charts
- [ ] container images on quay.io

## Getting started

```bash
git clone https://github.com/unclearParadigm/schmusek8ser
cd schmusek8ser
pip install -r requirements.txt
python3 -m main.py
```

### Configuration

`schmusek8ser` is configurable through environment variables. All configuration variables (as well as their defaults) are available in the [config.py](config.py)

| Variable                            | Data Type | Description                                                              |
|:------------------------------------|:----------|:-------------------------------------------------------------------------|
| SCHMUSEK8SER_LISTEN_PORT            | number    | the Listen TCP port of the HTTP API                                      |
| SCHMUSEK8SER_LISTEN_HOST            | string    | the Listen Host of the HTTP API (e.g. localhost)                         |
| SCHMUSEK8SER_AUTHORIZED_API_KEYS__0 | string    | an API key retreived through the `/apikey/new?for=<user>` endpoint       |
| SCMUSERK8SER_AUTHORIZED_API_KEYS__1 | string    | another API key - you can add more by incrementing the postfix           |
| SCMUSERK8SER_AUTHORIZED_API_KEYS__2 | string    | guess you get the idea now ^^                                            |
| SCHMUSEK8SER_K8S_KUBECONFIG_PATH    | string    | path to the kubeconfig used to authenticate to the K8s API               |
| SCHMUSEK8SER_K8S_KUBECONFIG_CTX     | string    | context that shall be used if kubeconfig contains more clusters          |
| SCHMUSEK8SER_NTFY_ENABLE            | bool      | whether to enable NTFY notification services                             |
| SCHMUSEK8SER_NTFY_BASE_URL          | string    | the ntfy server to use (by default uses [ntfy.rtrace.io](ntfy.rtrace.io) |
| SCHMUSEK8SER_NTFY_TOPIC             | string    | the topic the notifications should be pushed to (make sure to change)    |

## Contributing

Contributions to `schmusek8ser` are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

`schmusek8ser` is licensed under the MIT License, allowing you to use, modify, and distribute the software freely.
