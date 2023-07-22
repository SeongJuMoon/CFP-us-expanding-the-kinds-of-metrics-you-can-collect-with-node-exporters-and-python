#!/usr/bin/env python3

import platform
import os
from prometheus_client import CollectorRegistry, Gauge, generate_latest

FILENAME=list(filter(lambda f: f.endswith(".py"), __file__.split("/")))[0].split(".")[:1][0]

def _write_machine_info_required(registry, labelnames, labelset):
    g = Gauge('node_machine_info', "Node hardware info.", labelnames=labelnames, 
              registry=registry)
    g.labels(**labelset).set(0)


def _write_prom_expfmt(filename=None, expfmt=None):
    if not expfmt:
        return
    if not filename:
        filename = ''.join(__file__.split(".")[:1])
    
    with open(f'{filename}.prom', mode="w") as f:
        f.writelines(expfmt)

def _main():
    registry = CollectorRegistry()
    metrics_label = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.machine()
    }

    _write_machine_info_required(registry, labelnames=metrics_label.keys(),labelset=metrics_label)
    _write_prom_expfmt(filename=f'{os.environ["PROM_DIRCTORY"]}/{FILENAME}',expfmt=generate_latest(registry).decode())

if __name__ == "__main__":
    _main()