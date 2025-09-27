#!/bin/bash

# Loopback from Scarlett sound card to analog output with PulseAudio

# Manually start the module-loopback.
pactl load-module module-loopback
# Remap to mono sink to have sound on both ears
pactl load-module module-remap-sink sink_name=mono master=alsa_output.pci-0000_00_1f.5.analog-stereo channels=2 channel_map=mono,mono
