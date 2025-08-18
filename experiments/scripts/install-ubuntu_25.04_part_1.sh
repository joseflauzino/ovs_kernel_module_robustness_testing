# Kernel v6.14.6 on Ubuntu 25.04

## Prepare the system and install required packages

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libsqlite3-dev libffi-dev curl

## Install Linux kernel v6.14.6

KERNEL_VERSION="6.14.6"
ARCH="amd64"
BASE_URL="https://kernel.ubuntu.com/mainline/v${KERNEL_VERSION}/"

mkdir -p ~/kernels/v${KERNEL_VERSION}
cd ~/kernels/v${KERNEL_VERSION}

wget https://kernel.ubuntu.com/mainline/v6.14.6/amd64/linux-headers-6.14.6-061406_6.14.6-061406.202505090840_all.deb
wget https://kernel.ubuntu.com/mainline/v6.14.6/amd64/linux-headers-6.14.6-061406-generic_6.14.6-061406.202505090840_amd64.deb
wget https://kernel.ubuntu.com/mainline/v6.14.6/amd64/linux-image-unsigned-6.14.6-061406-generic_6.14.6-061406.202505090840_amd64.deb
wget https://kernel.ubuntu.com/mainline/v6.14.6/amd64/linux-modules-6.14.6-061406-generic_6.14.6-061406.202505090840_amd64.deb

sudo dpkg -i *.deb

sudo update-grub
sudo reboot
