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
### On the PC
- `git init && git pull` this repo on to the PC you would like to use as an remote controller.
 - Install a FTP server that has write permissions for a user chip with password chip to the folder `/home/chip`. This is where the webcam images will be uploaded. We used `vsftpd` from Ubuntu repositories with some configuring on permissions and write access. 
 - Make sure Python2.7 and Pygame are installed and run the `controller.py` sever script. If you want to test the experimental face follower functionality, also install `python-opencv`. 
 - Start the controller server with the command `python controller.py`.
 
### On the chip
- `git init && git pull` this repo on to the Chip controlling the robot and `cd` to the `onChip` folder.
 - Install `fswebcam` that is used to take pictures with the webcam.
 - In the file `pictureloop.sh` change the IP address on row 8 to point to the PC you are running your FTP server on.
 - In the file `rc.py` change the IP address on row 9 to point to the PC you are running your `controller.py` on.
 - Ensure that the server on the PC is still waiting for the client to connect and run the `pictureloop.sh`, which will start the `rc.py`and then start sending webcam pictures to the FTP server.
 
### The Face Homing Robot aka. "Terminator" mode
This is experimental feature that was implemented during the hackathon, but not completely finished tested. It might work OK... or not. It is based on the Haar cascade face recognitor that comes with OpenCV machine vision library. If the face follower is enabled the Chip robot will home towards a face it sees.
- Given that the package `python-opencv`is installed on the PC, press `e` on the controller application to toggle the face follower. Then tilt the robot webcam so that the robot sees some faces.
- Move away until the robot sees your face. Then it will turn and/or drive towards you until the tracking is lost. Beware, the robot will not stop for any obstacles if it gets a reading of a face.
- If left and right are mixed (the robot turns **away** from a face, change the rows 61,62,64,65 in the `controller.py´ and it is fixed!
