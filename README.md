# RE:BUILD

## Remote Controlled Robot Powered By C.H.I.P (Robot and API part)

Your task is to finish the robot and to build an API for controlling it. Provide API calls for basic movement first, and later
you can add combinations and tricks etc. Build camera stream to be used in controller application. Add some sort of authentication to make the system
secure. Provide good documentation for the group that is working with controller application for the same robot.

Focus on:
- Providing working API for robot's basic movement
- Good documentation for using the API
- Stream the camera to be used with front end
- Add more functionalities to API

## What we did

- Scrapped the PWM control in the example.py. The PWM was driving the L293D H-bridge chip, but it did not seem to put enough power to the ground. Also, using the PWM was unreliable: They got "stuck" and we had to power cycle the Chip to make them work again. Perhaps updating the library, redoing the wiring etc. could have helped, but time was premium in this hackathon, so we went to the simple option and replaced it with plain digital GPIO outputs.
- Implemented the `onChip/drive2.py` file that has the API for driving the robot using Python. It can be imported as a python module to gain access to the driving functions. If run as a script it provides a simple text based interface to controlling the thing (eg. ssh to Chip, run `sudo python drive2.py`. Note that `sudo` is required to gain access to the GPIO pins).
- Wrote a small TCP/IP Python client `onChip/rc.py`that runs on the Chip powered robot brain. 
- Strapped on a USB webcam on the robot platform and wrote a simple bash script `onChip/pictureloop.sh` to take a picture and upload it to hardcoded FTP server for processing and/or viewing. The script also starts the Python client that gets it's commands to drive the robot from (another or same) hardcoded server.
- Implemented a simple remote controller application with Python and Pygame that shows the image from the webcam that was stored on the FTP server and sends keypresses to the client script running on the 
- Implemented a face recognition that is running on the server. If `e`is pressed on 

## How to get it running
### On the chip
- `git init && git pull` this repo on to the PC you would like to use as an remote controller.
 - Install a FTP server that has write permissions for a user chip with password chip to the folder `/home/chip`. This is where the webcam images will be uploaded. We used `vsftpd` from Ubuntu repositories with some configuring on permissions and write access. 
- `git init && git pull` this repo on to the Chip controlling the robot. `cd` to the `onChip` folder, edit the rc.
