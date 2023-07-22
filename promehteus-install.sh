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
--set prometheus-node-exporter.sidecars[0].name="textfile" \
--set prometheus-node-exporter.sidecars[0].image="seongjumoon/textfile-collector:v1.0.0" \
--set prometheus-node-exporter.sidecars[0].args[0]=--path=/app/collector \
--set prometheus-node-exporter.sidecars[0].args[1]=--destpath=/run/prometheus \
--set prometheus-node-exporter.sidecarVolumeMount[0].name="collector-textfiles" \
--set prometheus-node-exporter.sidecarVolumeMount[0].mountPath="/run/prometheus" \
--set prometheus-node-exporter.sidecarVolumeMount[0].readOnly="false" \
--set prometheus-node-exporter.extraArgs[0]="--collector.textfile.directory=/run/prometheus" \
--namespace=monitoring \
--create-namespace
