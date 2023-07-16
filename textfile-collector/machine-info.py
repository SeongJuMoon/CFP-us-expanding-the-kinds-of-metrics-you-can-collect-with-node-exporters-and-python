#!/usr/bin/env python3

import platform
from prometheus_client import CollectorRegistry, Gauge, generate_latest

def _write_machine_info_required(registry):
    g = Gauge('node_machine_info', "Node hardware info.", labelnames=["architecture", ""] , 
              registry=registry)
    g.set(1)


def _main():
    registry = CollectorRegistry()
    metrics_label = {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "architecture": platform.machine()
    }

    _write_machine_info_required(registry)
    print(generate_latest(registry).decode(), end='')


if __name__ == "__main__":
    _main()