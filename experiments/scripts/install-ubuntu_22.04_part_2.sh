# Minimum required Python version
REQUIRED="3.8.10"

# Get installed version
INSTALLED=$(python3 --version 2>&1 | awk '{print $2}')

# Compare versions
if [ "$(printf '%s\n' "$REQUIRED" "$INSTALLED" | sort -V | head -n1)" != "$REQUIRED" ]; then
    echo "Python $REQUIRED or higher is required. Found: $INSTALLED"
    exit 1   # Stop the script
fi

echo "Python version $INSTALLED satisfies requirement (>= $REQUIRED)."

# Install Open vSwitch and Pip
sudo apt install -y openvswitch-common openvswitch-switch python3-pip

cd ../src/
sudo pip3 install -r requirements.txt
sudo python3 main.py -h
