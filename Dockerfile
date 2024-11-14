FROM python:alpine

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./main.py"]


LABEL org.opencontainers.image.title="schmusek8ser"
LABEL org.opencontainers.image.description="A simple CI/CD helper to deploy/update your Kubernetes workloads"
LABEL org.opencontainers.image.url="https://quay.io/repository/rtraceio/schmusek8ser"
LABEL org.opencontainers.image.authors="@ruffy@mastodon.social"
LABEL org.opencontainers.image.source="https://github.com/unclearParadigm/schmusek8ser"
LABEL org.opencontainers.image.documentation="https://github.com/unclearParadigm/schmusek8ser"
