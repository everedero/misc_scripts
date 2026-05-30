#!/bin/bash

# Loopback by using Pipewire GUI
apt install qpwgraph
qpwgraph

# Misc config, for instance to have minimal latency
vim /usr/share/pipewire/pipewire.conf
pw-top
