import os
from prometheus_client import CollectorRegistry, Gauge, generate_latest

def _write_os_info_required(registry):
    g = Gauge('node_reboot_required', "Node reboot is required for software updates.",
              registry=registry)
    g.set(int(os.path.isfile('/run/reboot-required')))


def _main():
    registry = CollectorRegistry()
    _write_os_info_required(registry)
    print(generate_latest(registry).decode(), end='')


if __name__ == "__main__":
    _main()