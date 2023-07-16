#!/usr/bin/env bash

export TOOLCHAINS="go"
export DOCKER_REPO="seongjumoon/node-exporter:v1.6.0-ubuntu2004.0"

function utils:tool:installed {
	command -v "$@" > /dev/null 2>&1
}

echo "check is assume prequirement."
for TOOLCHAIN in $TOOLCHAINS
do
    echo $TOOLCHAIN
    if ! utils:tool:installed $TOOLCHAIN; then
        echo -e  "please install prerequirment toolchain on your laptop.\n toolchain name is $TOOLCHAIN"
    fi
done
echo "check is assume prequirement finished."

echo "Bake custom node_export image."
echo "building node exporter fom git and golang"
git clone https://github.com/prometheus/node_exporter.git -b v1.6.0 .build
pushd .build
make build
popd
docker build . -t $DOCKER_REPO 
docker push $DOCKER_REPO
echo "Bake custom node_export image done "