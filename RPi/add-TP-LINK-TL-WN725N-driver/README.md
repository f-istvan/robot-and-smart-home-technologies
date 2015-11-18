How to install TP-Link TL-WN725N on Raspberry Pi. 

All you need:
* a RPi
* TP-Link TL-WN725N
* HDMI cable

Steps to set up a RPi with TP-Link TL-WN725N:

* Install Raspbian Wheezy
* First run using HDMI cable:
** Setup Raspbian Wheezy (no need to plug UTP calbe)
** After setup: $ sudo shutdown -h now
* Plug UTP calbe and start RPi
* find PRi's IP address
* ssh to Raspberry:
** $ ssh pi@<IP>
** defaults: user: ip, passwd: raspberry
* Find out our Raspbian Wheezy's version. Command: $ uname -a
* Find the right TP-LINK driver url here: https://www.raspberrypi.org/forums/viewtopic.php?p=462982#p462982
* Download the driver using wget command
* Find out how to install the driver
* Install the driver
* Check if instalation was successful: $ ifconfig