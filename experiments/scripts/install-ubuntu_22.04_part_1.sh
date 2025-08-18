# Kernel v5.19.9 on Ubuntu 22.04

## Prepare the system and install required packages

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libsqlite3-dev libffi-dev curl

## Install Linux kernel v5.19.9

KERNEL_VERSION="5.19.9"
ARCH="amd64"
BASE_URL="https://kernel.ubuntu.com/mainline/v${KERNEL_VERSION}/"

mkdir -p ~/kernels/v${KERNEL_VERSION}
cd ~/kernels/v${KERNEL_VERSION}

wget https://kernel.ubuntu.com/mainline/v5.19.9/amd64/linux-headers-5.19.9-051909_5.19.9-051909.202209220718_all.deb
wget https://kernel.ubuntu.com/mainline/v5.19.9/amd64/linux-headers-5.19.9-051909-generic_5.19.9-051909.202209220718_amd64.deb
wget https://kernel.ubuntu.com/mainline/v5.19.9/amd64/linux-image-unsigned-5.19.9-051909-generic_5.19.9-051909.202209220718_amd64.deb
wget https://kernel.ubuntu.com/mainline/v5.19.9/amd64/linux-modules-5.19.9-051909-generic_5.19.9-051909.202209220718_amd64.deb

sudo dpkg -i *.deb

sudo sed -i 's/GRUB_DEFAULT=0/GRUB_DEFAULT="1>4"/' /etc/default/grub
sudo update-grub
sudo reboot
