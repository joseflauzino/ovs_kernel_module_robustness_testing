# Kernel v4.20.9 on Ubuntu 19.04

## Prepare the system and install required packages

sudo bash -c 'cat > /etc/apt/sources.list <<EOF
deb http://old-releases.ubuntu.com/ubuntu disco main restricted
deb http://old-releases.ubuntu.com/ubuntu disco-updates main restricted
deb http://old-releases.ubuntu.com/ubuntu disco-security main restricted

deb http://old-releases.ubuntu.com/ubuntu disco main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu disco-updates main restricted universe multiverse
deb http://old-releases.ubuntu.com/ubuntu disco-security main restricted universe multiverse
EOF'

sudo apt update -y
sudo apt upgrade -y
sudo apt install -y zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libsqlite3-dev libffi-dev curl git

## Install Linux kernel v4.20.9

KERNEL_VERSION="4.20.9"
ARCH="amd64"
BASE_URL="https://kernel.ubuntu.com/mainline/v${KERNEL_VERSION}/"

mkdir -p ~/kernels/v${KERNEL_VERSION}
cd ~/kernels/v${KERNEL_VERSION}

wget https://kernel.ubuntu.com/mainline/v4.20.9/linux-headers-4.20.9-042009_4.20.9-042009.201902150331_all.deb
wget https://kernel.ubuntu.com/mainline/v4.20.9/linux-headers-4.20.9-042009-generic_4.20.9-042009.201902150331_amd64.deb
wget https://kernel.ubuntu.com/mainline/v4.20.9/linux-image-unsigned-4.20.9-042009-generic_4.20.9-042009.201902150331_amd64.deb
wget https://kernel.ubuntu.com/mainline/v4.20.9/linux-modules-4.20.9-042009-generic_4.20.9-042009.201902150331_amd64.deb

sudo dpkg -i *.deb

sudo sed -i 's/GRUB_DEFAULT=0/GRUB_DEFAULT="1>4"/' /etc/default/grub
sudo update-grub
sudo reboot
