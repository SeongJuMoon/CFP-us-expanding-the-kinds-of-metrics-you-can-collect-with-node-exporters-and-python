FROM ubuntu:20.04

ENV DEBIAN_FRONTEND="noninteractive"
RUN apt-get update -y && apt-get install python3-pip -y
COPY .build/node_exporter /bin/node_exporter
COPY infra/requirments.txt .
COPY  --chown=65536:65536 textfile-collector /etc/prometheus/textfile-collector

EXPOSE      9100
USER        nobody

ENTRYPOINT  [ "/bin/node_exporter" ]