#!/bin/bash

cd ../src/

# Extract ID and VERSION_ID
. /etc/os-release

if [ "$ID" != "ubuntu" ]; then
    echo "This system is not Ubuntu (found: $ID)"
    exit 1
fi

PYTHON_CMD="python3"

if [[ "$VERSION_ID" == "15.04" || "$VERSION_ID" == "19.04" ]]; then
    PYTHON_CMD="python3.8" # explicitly mention Python 3.8 version
fi

sudo $PYTHON_CMD main.py -f ovs_datapath
sudo $PYTHON_CMD main.py -f ovs_packet

if [ "$VERSION_ID" != "15.04" ]; then
    sudo $PYTHON_CMD main.py -f ovs_vport
    sudo $PYTHON_CMD main.py -f ovs_flow
    sudo $PYTHON_CMD main.py -f ovs_meter
    sudo $PYTHON_CMD main.py -f ovs_ct_limit
else
    echo "Skipping families that could not be tested on Ubuntu 15.04."
fi