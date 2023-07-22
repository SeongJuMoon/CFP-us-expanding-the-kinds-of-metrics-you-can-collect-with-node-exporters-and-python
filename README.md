# Expanding-the-kinds-of-metrics-you-can-collect-with-node-exporters-and-python

# Prerequisites
- helm (v3.6+)
- docker (20.10.21+)

# How to simulate configured demo environment?
1. Run build.sh to bake custom node-exporter image.
```bash
./build.sh 
```

2. Run to deploy prometheus-stack using helm.
```bash
./promehteus-install.sh
```

3. check metrics added from node_exporter. 
```bash
query metrics node_reboot_required
```
