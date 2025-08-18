## Install Python 3.6

cd /tmp
wget https://www.python.org/ftp/python/3.6.15/Python-3.6.15.tgz
tar -xzf Python-3.6.15.tgz
cd Python-3.6.15
./configure --prefix=/usr/local
make -j$(nproc)
sudo make altinstall

python3.6 --version # outpt: Python 3.6.15

# Install Open vSwitch
sudo apt install -y openvswitch-common openvswitch-switch

cd ../../src/
sudo pip3.6 install -r requeriments.txt
sudo python3.6 main.py -h
