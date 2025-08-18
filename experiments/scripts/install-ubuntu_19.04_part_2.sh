#!/bin/bash

## Install Python 3.8.10
cd /tmp
wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tgz
tar -xf Python-3.8.10.tgz
cd Python-3.8.10
./configure --enable-optimizations
make -j $(nproc)
sudo make altinstall

# Minimum required Python version
REQUIRED="3.8.10"

# Get installed version
INSTALLED=$(python3.8 --version 2>&1 | awk '{print $2}')

# Compare versions
if [ "$(printf '%s\n' "$REQUIRED" "$INSTALLED" | sort -V | head -n1)" != "$REQUIRED" ]; then
    echo "Python $REQUIRED or higher is required. Found: $INSTALLED"
    exit 1   # Stop the script
fi

echo "Python version $INSTALLED satisfies requirement (>= $REQUIRED)."

# Install Open vSwitch
sudo apt install -y openvswitch-common openvswitch-switch

cd ../src/
sudo pip3.8 install -r requirements.txt
sudo python3.8 main.py -h
