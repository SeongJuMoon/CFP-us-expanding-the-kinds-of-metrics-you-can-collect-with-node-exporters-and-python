#!/usr/bin/env python3
#
# Description: Expose metrics from rpm installed sofrware.
#
# Dependencies: prometheus_client
#
# Authors: Seongju Moon <seongju.moon@linux.com>


import re
import os
from prometheus_client import CollectorRegistry, Gauge, generate_latest

def _get_rpm_package_list_from_system():
    f = os.popen('rpm -qa')
    raw_rpm_installed_software_list=f.readlines()
    return raw_rpm_installed_software_list

def _transform(rpm):
        pattern = r"^(.+)-([\d\.]+)-([\w\.]+)(?:\.(\w+))?$"
        match = re.match(pattern, rpm)
        if match:
            package_name = match.group(1)
            version = match.group(2)
            release = match.group(3)
            architecture = match.group(4)

            return {
            'name': package_name,
            'version': version,
            'release': release,
            "architecture": architecture
        }
        else:
            raise RuntimeError(f"can't parse rpm format {rpm}")
        

def _write_rpm_package_installed(registry, rpm_packages):
    g = Gauge('node_installed', "Node reboot is required for software updates.", labelnames=['name', 'version', 'release', 'architecture'],
              registry=registry)
    for rpm_package in rpm_packages:
        package=_transform(rpm_package)
        print(package)
        g.labels(**package).set(1)
    

def _main():
    registry = CollectorRegistry()

    rpm_packages = []
    if os.environ.get('DEBUG', 'false').lower() == 'true':
        rpm_packages = [
            "kbd-legacy-1.15.5-16.el7_9.noarch",
            "gcc-4.8.5-44.el7.x86_64",
            "yum-3.4.3-168.el7.centos.noarch",
            "NetworkManager-tui-1.18.8-2.el7_9.x86_64",
            "nfs-utils-1.3.0-0.68.el7.2.x86_64",
            "grub2-2.02-0.87.0.2.el7.centos.11.x86_64",
            "openssh-server-7.4p1-22.el7_9.x86_64",
        ]
    else:
        rpm_packages = _get_rpm_package_list_from_system()
        

    
    _write_rpm_package_installed(registry, rpm_packages)

    print(generate_latest(registry).decode(), end='')


if __name__ == "__main__":
    _main()
    # output
    # node_installed{architecture="noarch",name="kbd-legacy",release="5-16.el7_9",version=".15.5-16.el7_9.noarch"} 1.0
    # node_installed{architecture="x86_64",name="gcc",release="5-44.el7",version=".8.5-44.el7.x86_64"} 1.0
    # node_installed{architecture="noarch",name="yum",release="3-168.el7.centos",version=".4.3-168.el7.centos.noarch"} 1.0
    # node_installed{architecture="x86_64",name="NetworkManager-tui",release="8-2.el7_9",version=".18.8-2.el7_9.x86_64"} 1.0
    # node_installed{architecture="x86_64",name="nfs-utils",release="0-0.68.el7.2",version=".3.0-0.68.el7.2.x86_64"} 1.0
    # node_installed{architecture="x86_64",name="grub2",release="87.0.2.el7.centos.11",version=".02-0.87.0.2.el7.centos.11.x86_64"} 1.0
    # node_installed{architecture="x86_64",name="openssh-server",release="el7_9",version=".4p1-22.el7_9.x86_64"} 1.0