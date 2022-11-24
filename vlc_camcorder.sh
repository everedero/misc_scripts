#!/bin/bash

#Script to record a webcam image every minute

echo 'This script records webcam image every 60 seconds'

for i in {1..120}
do
	rm -rf temp*.png
	echo 'Iter number '$i'...'
	timeout 5 vlc -I dummy v4l2:///dev/video0 --video-filter scene --no-audio --scene-path . --scene-prefix temp --scene-format png vlc://quit --run-time=1
	mv temp00001.png 'img'$i'.png'
	sleep 60
done
