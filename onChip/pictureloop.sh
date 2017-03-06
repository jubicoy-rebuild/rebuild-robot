#!/bin/bash
(python ./rc.py)&

i=1
while true
do
	fswebcam -r 640x480 --jpeg 50 -D 0 process_me.jpg
	ftp-upload -h 192.168.0.21 -u chip -d /home/chip --password chip process_me.jpg
        ((i++))
	#sleep 0.5 # sleep for 500 ms
done
