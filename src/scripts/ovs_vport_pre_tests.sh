#!/bin/bash

# Add two virtual interface
ip link add vport1 type veth

# Enable the virtual interface
ip link set vport1 up

# Add datapath
ovs-dpctl add-dp dp-default-name
