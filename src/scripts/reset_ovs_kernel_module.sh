#!/bin/bash

# Ensure the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Error: This script must be run as root." >&2
    exit 1
fi

# Get a list of all existing datapaths
datapaths=$(ovs-dpctl dump-dps)

# Check if there are any datapaths
if [ -z "$datapaths" ]; then
    echo "No datapaths found."
else
    # Remove each datapath
    for dp in $datapaths; do
        echo "Removing datapath: $dp"
        ovs-dpctl del-dp "$dp"
    done
    echo "All datapaths removed."
fi

# Ensure all operations are committed before reloading the module
sync

# Disable the Open vSwitch kernel module
echo "Disabling the Open vSwitch kernel module..."
if ! modprobe -r openvswitch; then
    echo "Error: Failed to unload the Open vSwitch kernel module." >&2
    exit 1
fi

# Enable the Open vSwitch kernel module
echo "Enabling the Open vSwitch kernel module..."
if ! modprobe openvswitch; then
    echo "Error: Failed to load the Open vSwitch kernel module." >&2
    exit 1
fi

# Finish
echo "Open vSwitch kernel module reset process complete."
exit 0
