# Kernel v3.19.8 on Ubuntu 15.04

## Prepare the system and install required packages

sudo bash -c 'cat > /etc/apt/sources.list <<EOF
deb http://old-releases.ubuntu.com/ubuntu vivid main restricted
deb http://old-releases.ubuntu.com/ubuntu vivid-updates main restricted
deb http://old-releases.ubuntu.com/ubuntu vivid-security main restricted

deb http://old-releases.ubuntu.com/ubuntu vivid main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu vivid-updates main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu vivid-security main restricted universe multiverse
EOF'

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libsqlite3-dev libffi-dev curl git

## Install Linux kernel v3.19.8

KERNEL_VERSION="3.19.8"
ARCH="amd64"
BASE_URL="https://kernel.ubuntu.com/mainline/v${KERNEL_VERSION}/"

mkdir -p ~/kernels/v${KERNEL_VERSION}
cd ~/kernels/v${KERNEL_VERSION}

wget https://kernel.ubuntu.com/mainline/v3.19.8-ckt23/linux-headers-3.19.8-031908ckt23_3.19.8-031908ckt23.201607121433_all.deb --no-check-certificate
wget https://kernel.ubuntu.com/mainline/v3.19.8-ckt23/linux-headers-3.19.8-031908ckt23-generic_3.19.8-031908ckt23.201607121433_amd64.deb --no-check-certificate
wget https://kernel.ubuntu.com/mainline/v3.19.8-ckt23/linux-image-3.19.8-031908ckt23-generic_3.19.8-031908ckt23.201607121433_amd64.deb --no-check-certificate

sudo dpkg -i *.deb

sudo reboot
