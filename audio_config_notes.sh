#!/bin/bash

# Loopback from Scarlett sound card to analog output with PulseAudio

# Manually start the module-loopback.
pactl load-module module-loopback
# Find the audio output name
pactl list sinks short
# Remap to mono sink to have sound on both ears
pactl load-module module-remap-sink sink_name=mono master=alsa_output.pci-0000_00_1f.N.analog-stereo channels=2 channel_map=mono,mono

# Cleanup when done
pactl unload-module module-remap-sink
pactl unload-module module-loopback

# Module loopback sometimes get stuck
# Loopback by using Pipewire GUI
apt install qpwgraph
qpwgraph
