#!/usr/bin/env python3

import os
from prometheus_client import CollectorRegistry, Gauge, generate_latest

FILENAME=list(filter(lambda f: f.endswith(".py"), __file__.split("/")))[0].split(".")[:1][0]

def _write_os_info_required(registry):
    g = Gauge('node_reboot_required', "Node reboot is required for software updates.",
              registry=registry)
    g.set(int(os.path.isfile('/run/reboot-required')))

def _write_prom_expfmt(filename=None, expfmt=None):
    if not expfmt:
        return
    if not filename: # in directory
        filename = ''.join(__file__.split(".")[:1])
        
    with open(f'{filename}.prom', mode="w") as f:
        f.writelines(expfmt)


def _main():
    registry = CollectorRegistry()
    _write_os_info_required(registry)
    _write_prom_expfmt(filename=f'{os.environ["PROM_DIRCTORY"]}/{FILENAME}',expfmt=generate_latest(registry).decode())


if __name__ == "__main__":
    _main()