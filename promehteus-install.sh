#!/usr/bin/env bash

helm upgrade -i prometheus-stack prometheus-community/kube-prometheus-stack  \
--set defaultRules.create="true" \
--set defaultRules.rules.alertmanager="false" \
--set alertmanager.enabled="false" \
--set prometheus.service.type="LoadBalancer" \
--set server.service.loadBalancerIP="192.168.1.11" \
--set prometheus.service.port="80" \
--set prometheus.prometheusSpec.scrapeInterval="15s" \
--set prometheus.prometheusSpec.evaluationInterval="15s" \
--set prometheus-node-exporter.image.registry="index.docker.io" \
--set prometheus-node-exporter.image.repository="seongjumoon/node-exporter" \
--set prometheus-node-exporter.image.tag="v1.6.0-ubuntu2004.0" \
--set prometheus-node-exporter.image.pullPolicy="IfNotPresent" \
--namespace=monitoring \
--create-namespace
