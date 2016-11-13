### How to install Raspberry Pi with TP-Link TL-WN725N Wireless USB Adapter. 

#### All you need
* a RPi
* TP-Link TL-WN725N

#### Steps
* download Raspbian Jessie Lite (Linux raspberrypi 4.4.21+ #911 Thu Sep 15 14:17:52 BST 2016 armv6l GNU/Linux - conatins the driver for TP-Link TL-WN725N Wireless USB Adapter
)
* Format your sd card to FAT32 (e.g.: using GParted)
* Install Raspbian Jessie Lite form terminal with dd
* start RPi
* find out your RPi's IP address
* connect to it with ssh
  * user: pi
  * passwd: raspberry

#### Useful Commands and tips
* Always shutdown your RPi with:

```sh
$ sudo shutdown -h now
```