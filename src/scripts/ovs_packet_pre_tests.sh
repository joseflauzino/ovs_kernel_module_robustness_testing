#!/bin/bash

# Add two virtual interfaces
ip link add vport1 type veth
ip link add vport2 type veth

# Enable the virtual interfaces
ip link set vport1 up
ip link set vport2 up

# Add datapath
ovs-dpctl add-dp dp-default-name

# Add virtual interfaces to the datapath as vports
ovs-dpctl add-if dp-default-name vport1
ovs-dpctl add-if dp-default-name vport2

# Add a flow rule
ovs-dpctl add-flow "ufid:6bb38b00-00b9-4c7f-a7b4-b1a1b57d1fd1,in_port(1),eth(),eth_type(0x806),arp()" 2
