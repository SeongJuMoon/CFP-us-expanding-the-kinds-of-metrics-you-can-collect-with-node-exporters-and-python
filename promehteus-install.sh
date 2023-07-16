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
--set prometheus-node-exporter.image="seongjumoon/node-exporter:v1.6.0-ubuntu20.04" \
--namespace=monitoring \
--create-namespace
