[![AUR](https://img.shields.io/aur/license/yaourt.svg?maxAge=2592000?style=flat-square)](https://raw.githubusercontent.com/rahulranjan96/TextMiner/master/LICENSE.txt?token=APHqCzbjidKXSG9I056xLviUt6URhmBtks5XZ6kYwA%3D%3D)

SmartRack 1.0
==============

Raspberry-Pi Setup
------------------

#Platforms
This project has been built upon Raspberry Pi 2.0 using Raspbian Jessie OS.

#Proxy Settings:
###Setting proxy authentication in apt.conf file:
```
$ sudo nano /etc/apt/apt.conf
```
Add following lines in the file:
```
Acquire::http::proxy "http://username:password@proxy:port/";
Acquire::https::proxy "https://username:password@proxy:port/";
Acquire::ftp::proxy "ftp://username:password@proxy:port/";
Acquire::socks::proxy "socks://username:password@proxy:port/";

```
###Setting proxy authentication in environment file:
```
$ sudo nano /etc/environment
```
Add following lines in the file:
```
http_proxy="http://username:password@proxy:port/"
https_proxy="https://username:password@proxy:port/"
ftp_proxy="ftp://username:password@proxy:port/"
socks_proxy="socks://username:password@proxy:port/"
```
###Setting proxy authentication in bash file:
```
$ sudo nano ~/.bashrc

```
Add following lines at the last line of the file:
```
export {http,https,ftp}_proxy='http://username:password@proxy:port'

```

#Dependencies Installations:
We are using various Python Libraries and other open-source softwares.

###The code for this project has been written in Python3.4 and Python3.4 is required to run it.
To install Python3.4
```
$ sudo apt-get install python3

```
To install pip3 which will be further used to install other python libraries.
```
$ sudo apt-get install python3-pip

```
###For Image Processing this project uses python [scikit-image](http://scikit-image.org/) library and its dependecies.
To install scikit-image library and its dependecies :
```
$ sudo pip3 install numpy scipy scikit-image
```
###For Speech Processing this project uses python [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition/) library and its dependecies.
To install SpeechRecognition library and its dependencies:
```
$ git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
$ cd pyaudio
$ sudo python3 setup.py install
$ cd ..
$ rm -rf pyaudio/
$ sudo apt-get installl libportaudio-dev
$ sudo apt-get install python3-dev
$ sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
$ sudo pip3 install SpeechRecognition
```
###For Text To Speech Conversion this project uses speak synthesiser software [espeak](http://espeak.sourceforge.net/).
```
$ sudo apt-get install espeak
```
#To download and run this application

###Clone this reository:
```
$ git clone https://github.com/rahulranjan96/SmartRack.git
```
###To run this application:

```
$ cd SmartRack
$ python3 main.py

```

Arduino Setup
-------------
