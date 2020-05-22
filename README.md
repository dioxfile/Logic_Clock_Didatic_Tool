# Vector_Clock

![alt text](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/QRCode_Vector_clock.png)

Code in Python to synchronize the computer clock using the [Lamport](https://en.wikipedia.org/wiki/Leslie_Lamport) method.

People use the physical time to order events. For example, we say that an event at 8:15 AM occurs before an event at 8:16 AM. In distributed systems, physical clocks are not always precise, so we can't rely on physical time to order events. Instead, we can use logical clocks to create a partial or total ordering of events. This article explores the concept of and implementation of the logical clocks invented by Leslie Lamport in his seminal paper Time, Clocks, and the Ordering of Events in a Distributed System.

![animacao](https://user-images.githubusercontent.com/32453979/47199699-d9c90e00-d340-11e8-94b7-6b609d44561e.gif)


1. [What are the Possible Applications?](#What-are-the-Possible-Applications)
1. [Methodology](#methodology)
1. [Prerequisites](#prerequisites)
1. [What do you need to use this software?](#What-do-you-need-to-use-this-software)
1. [How to install it?](#how-to-install-it)
1. [Possibles errors](#possibles-errors)
1. [How to use it?](#How-to-use-it)


</head>

# What are the Possible Applications?
Its purpose is the synchronization of logical clocks of computers connected to the same network.

## Methodology.
* OS: Ubuntu 18.04 cosmic
* Kernel: x86_64 Linux 4.18.0-10-generic
* CPU: Intel Core i7 Q 740 @ 8x 1.734GHz
* GPU: GeForce GT 425M
* RAM: 7956MiB <br/> 

* __Test hardware:__ Intel (R) Pentium 4 (TM) 3.0 GHz, 1 GB RAM, HD 40 GB, 10/100 Fast Ethernet network
* __Test realize:__ The tests were performed in a _testbed_ with 8 computers in the _Laboratory of Computer Networks (UNEMAT)_, and all the computers of the laboratory were configured in a network class A 113.167.9.0/24 . In order to synchronize, the software takes into account the time correct at the highest hour. In this way, the clocks of the test machines were manually and randomly delayed.

# Prerequisites
* Pyhton2.7
* Idle-Python2.7
* Python-Dateutil
* Python-Netifaces
* Python-Ipaddr
* Python-WXgtk2.8


# What do you need to use this software?
* You will need a GNU/Linux Ubuntu 18.04.1 cosmic; Debian 9.5 Stretch or the Arch Linux x86_64.
* Internet connection for download.

Probably the software will also work on any other Debian-based or the Arch Linux-base distribution, but it has only been tested on the systems listed above.


* For x86_64 debian-based distributions<br/> 
These are the necessary packages and modules.
The version may not necessarily be the same, but these versions have been tested and confirmed the operation.

* 1. PYTHON IDLE <br/>
Package: idle-python2.7 <br/>
Version: 2.7.12-1ubuntu0~16.04.3 <br/>

* 2. PIP<br/>
Package: python-pip<br/>
Version: 8.1.1-2ubuntu0.4 <br/>

* 3. DATEUTIL<br/>
Package: python-dateutil<br/>
Version: 2.4.2-1<br/>

* 4. NETIFACES<br/>
Package: python-netifaces<br/>
Version: 0.10.4-0.1build2<br/>

* 5. IPADDR<br/>
Package: python-ipaddr<br/>
Version: 2.1.11-2<br/>

* 6. LIBPNG<br/>
Package: libpng12-0<br/>
Version: 1.2.54-1ubuntu1.1<br/>

* 7. LIBTIFF<br/>
Package: libtiff4<br/>
Version: 3.9.6-11+deb7u11<br/>

* 8. LIBWXBASE<br/>
Package: libwxbase2.8-0<br/>
Version: 2.8.12.1-12<br/>

* 9. LIBWXGTK<br/>
Package: libwxgtk2.8-0<br/>
Version: 2.8.12.1-12<br/>

* 10. XWPYTHON<br/>
Package: python-wxgtk2.8<br/>
Version: 2.8.12.1-12<br/>
***********************************************************************************************

* For x86 debian-based distributions.<br/> 
The version may not necessarily be the same, but these versions have been tested and confirmed the operation.

* 1. PYTHON IDLE <br/>
Package: idle-python2.7 <br/>
Version: 2.7.12-1ubuntu0~16.04.3 <br/>

* 2. PIP<br/>
Package: python-pip<br/>
Version: 8.1.1-2ubuntu0.4 <br/>

* 3. DATEUTIL<br/>
Package: python-dateutil<br/>
Version: 2.4.2-1<br/>

* 4. NETIFACES<br/>
Package: python-netifaces<br/>
Version: 0.10.4-0.1build2<br/>

* 5. IPADDR<br/>
Package: python-ipaddr<br/>
Version: 2.1.11-2<br/>

* 6. LIBPNG<br/>
Package: libpng12-0<br/>
Version: 1.2.54-1ubuntu1.1<br/>

* 7. LIBTIFF<br/>
Package: libtiff4<br/>
Version: 3.9.6-11+deb7u11<br/>

* 8. LIBWXBASE<br/>
Package: libwxbase2.8-0<br/>
Version: 2.8.12.1-12<br/>

* 9. LIBWXGTK<br/>
Package: libwxgtk2.8-0<br/>
Version: 2.8.12.1-12<br/>

* 10. XWPYTHON<br/>
Package: python-wxgtk2.8<br/>
Version: 2.8.12.1-12<br/>

* 11. LIBJPEG8<br/>
Package: libjpeg8<br/>
Version: 8c-2ubuntu8<br/>

* 12. LIBGSTREAMER<br/>
Package: libgstreamer0.10-0<br/>
Version: 0.10.36-1.5ubuntu1<br/>

* 12. LIBGSTREAMER-PLUGIN-BASE<br/>
Package: libgstreamer-plugins-base0.10-0<br/>
Version: 0.10.36-2<br/>

* 12. LIBWXGTK-MEDIA<br/>
Package: libwxgtk-media2.8-0<br/>
Version: 2.8.12.1+dfsg2-2ubuntu2+1-webupd8-xenial0<br/>

***********************************************************************************************

* For x86_64 Arch Linux-based distributions.<br/> 
Before starting with Arch, it is important that the installation of some libraries and packages required the use of community sources (AUR), which are similar to PPA utilities in ubuntu. Why the package has to be compiled in the machine, which ends up requiring more time than in the distributions without Debian.<br/> 

* 1. GSTREAMER0.10<br/> 
Package: gstreamer0.10<br/> 
Version: 0.10.36-17<br/> 

* 2. GSTREAMER0.10-BASE<br/> 
Package: gstreamer0.10-base<br/> 
Version: 0.10.36-11<br/> 

* 3. wxgtk2.8<br/> 
Package: wxgtk2.8<br/> 
Version: 2.8.12.1-6<br/> 

* 4. WXPYTHON-GTK2<br/> 
Package: wxpython-gtk2<br/> 
Version: 	3.0.2.0-6<br/>

* 5. WXPYTHON2.8<br/> 
Package: wxpython2.8<br/> 
Version: 2.8.12.1-3<br/>

* 6. PYTHON2-DATEUTIL<br/> 
Package: python-dateutil<br/> 
Version: 2.8.0-1<br/>

* 7. PYTHON2-NETIFACES<br/> 
Package: python-netifaces<br/> 
Version: 0.10.9-1<br/>

* 7. PYTHON2-IPADDR<br/> 
Package: python-ipaddr <br/> 
Version: 2.2.0-1<br/>


***********************************************************************************************
# How to install it?

* For x86_64 and 86x<br/>
Give permission to file INSTALL.sh<br/>
`$sudo chmod +x INSTALL.sh`

Obs: For the above command to work the terminal must be open where the file is located.<br/>

Run the file<br/>
`$sudo ./INSTALL.sh`

***********************************************************************************************
* You can do an installation automatically by running the file 'INSTALL.sh'. But if you want to install manually just follow the steps below.

* In Debian and Ubuntu.

First you will download the package and later install it.

Once the installations are finished you can delete the downloaded .deb files.


1. INSTALL PYTHON IDLE<br/>
`$sudo apt install idle-python2.7`<br/>

2. INSTALE PIP<br/>
`$sudo apt install python-pip`<br/>

3. INSTALL DATEUTIL (PIP)<br/>
`$sudo pip install python-dateutil`<br/>

4. INSTALL NETIFACES (PIP)<br/>
`$sudo pip install netifaces`<br/>

5. INSTALL IPADDR<br/>
`$sudo apt install python-ipaddr`<br/>

6. DOWNLOAD LIBPNG<br/>
`$sudo wget http://ftp.us.debian.org/debian/pool/main/libp/libpng/libpng12-0_1.2.49-1+deb7u2_amd64.deb`<br/>
6.1. INSTALL LIBPNG<br/>
`$sudo dpkg -i libpng12-0_1.2.49-1+deb7u2_amd64.deb`<br/>

7. DOWNLOAD LIBTIFF<br/>
`$sudo wget http://security.debian.org/debian-security/pool/updates/main/t/tiff3/libtiff4_3.9.6-11+deb7u11_amd64.deb`<br/>
7.1 INSTALL LIBTIFF<br/>
`$sudo dpkg -i libtiff4_3.9.6-11+deb7u11_amd64.deb`<br/>

8. DOWNLOAD LIBWXBASE<br/>
`$sudo wget http://ftp.us.debian.org/debian/pool/main/w/wxwidgets2.8/libwxbase2.8-0_2.8.12.1-12_amd64.deb`<br/>
8.1. INSTALL LIBWXBASE<br/>
`$sudo dpkg -i libwxbase2.8-0_2.8.12.1-12_amd64.deb`<br/>

9. DOWNLOAD LIBWXGTK<br/>
`$sudo wget http://ftp.us.debian.org/debian/pool/main/w/wxwidgets2.8/libwxgtk2.8-0_2.8.12.1-12_amd64.deb`<br/>
9.1. INSTALL LIBWXGTK<br/>
`$sudo dpkg -i libwxgtk2.8-0_2.8.12.1-12_amd64.deb`<br/>

10. DOWLOAD XWPYTHON<br/>
`$sudo wget http://ftp.us.debian.org/debian/pool/main/w/wxwidgets2.8/python-wxgtk2.8_2.8.12.1-12_amd64.deb`<br/>
10.1. INSTALL ALL DEPENDENCIES MISSING<br/>
`$sudo apt-get install -f`<br/>
10.2. INSTALL XWPYTHON<br/>
`$sudo dpkg -i python-wxgtk2.8_2.8.12.1-12_amd64.deb`<br/>

***********************************************************************************************
* In Arch<br/>

1. DOWNLOAD GSTREAMER0.10<br/>
`$wget https://aur.archlinux.org/cgit/aur.git/snapshot/gstreamer0.10.tar.gz`<br/>
1.2 EXTRACT THE PACKAGE<br/>
`$tar -xvf gstreamer0.10.tar.gz`<br/>
1.3 INSTALL<br/>
`$makepkg -si`<br/>

2. DOWNLOAD GSTREAMER0.10-BASE<br/>
`$wget https://aur.archlinux.org/cgit/aur.git/snapshot/gstreamer0.10-base.tar.gz`<br/>
2.2 EXTRACT THE PACKAGE<br/>
`$tar -xvf gstreamer0.10-base.tar.gz`<br/>
2.3 INSTALL<br/>
`$makepkg -si`<br/>

3. DOWNLOAD WXGTK2.8<br/>
`$wget https://aur.archlinux.org/cgit/aur.git/snapshot/wxgtk2.8.tar.gz`<br/>
3.2 EXTRACT THE PACKAGE<br/>
`$tar -xvf wxgtk2.8.tar.gz`<br/>
3.3 INSTALL<br/>
`$makepkg -si`<br/>

4. DOWNLOAD WXPYTHON-GTK2<br/>
`$wget https://aur.archlinux.org/cgit/aur.git/snapshot/wxpython-gtk2.tar.gz`<br/>
4.2 EXTRACT THE PACKAGE<br/>
`$tar -xvf wxpython-gtk2.tar.gz`<br/>
4.3 INSTALL<br/>
`$makepkg -si`<br/>

5. DOWNLOAD WXPYTHON2.8<br/>
`$wget https://aur.archlinux.org/cgit/aur.git/snapshot/wxpython-gtk2.tar.gz`<br/>
6.2 EXTRACT THE PACKAGE<br/>
`$tar -xvf wxpython2.8.tar.gz`<br/>
6.3 INSTALL<br/>
`$makepkg -si`<br/>

7. INSTALL DATEUTIL <br/>
`$sudo pacman -S python2-dateutil`<br/>

8. INSTALL NETIFACES <br/>
`$sudo pacman -S python2-netifaces`<br/>

9. INSTALL IPADDR<br/>
`$sudo pacman -S python2-ipaddr`<br/>


***********************************************************************************************



# Possibles errors

* If any module for unknown reasons has not been installed

Any module error that you may have to re-view the "HOW TO USE" session and manually install each module in sequence according to the tutorial. Follow steps 1 through 10.2.<br/>

In the Debian system, you may have a user error<br/>
If you get the error "./INSTALL.sh: sudo: not found". By default sudo is not installed, but you can install it. <br/>

First enable su-mode:<br/>
`$su`<br/>
 
Install sudo<br/>
`#apt install sudo -y`<br/>

After that you would need to play around with users and permissions. Give sudo right to your own user.<br/>
`#usermod -aG sudo yoursername`<br/>

Edit the file 'sudoers'<br/>
`#nano /etc/sudoers`<br/>

#User privilege specification<br/>
```shellcript
root ALL=(ALL:ALL) ALL<br/>
"yoursername" ALL=(ALL:ALL) ALL <br/><br/>
```
#The top line was the one we added. <br/>
#Replace 'yoursername' with the name of your user who wants to have root permission<br/>
`#exit`

* update error

Obs: In some cases Debian, when new, in the updates configuration file "/etc/apt/sources.list", the line referring to the cdrom is not commented out, this causes an error at the time of the update and consequently when installing some programs and libraries with apt.
It is advisable to comment on any lines referring to the use of "cdrom" sources, and it is strongly recommended to use official Debian sources, both "Debian" and "security".

![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/gif-animada.gif)

***********************************************************************************************

# How to use it?

*  IMPORTANT: For the hours to change you must have root permission or be the root user.<br/>

Start from terminal<br/>
`#vectorclock`<br/>

OR<br/>

Start from your system menu<br/>

OR<br/>

Open 'idle-python', it must have root permission<br/>
`$sudo idle-python2.7`<br/>
or<br/>
`#idle python2.7`<br/><br/>

Click on 'File ==> Open ==> ds_logic_clocks_mc.py'<br/><br/>

The source code will appear on your screen<br/><br/>

Click on 'run ==> run module'<br/>
or<br/>
Press 'F5'<br/>
**************************************************************
The simplest way to use eh the "Broadcast"<br/>

* 1 - Shows the time that is "wrong"<br/>

* 2 - Click "Bind IP/Port" to make a connection<br/>

* 3 - You can choose between automatic and manual<br/>
Automatic: Send a message every 3 seconds<br/>
Manual: Send a message each time you click on it<br/>

* 4 - Note that the time has changed, important to realize that it has changed to an hour higher than it was already. Your time is now synchronized.<br/>

![animacao](https://user-images.githubusercontent.com/32777186/47819566-48d73700-dd31-11e8-87e7-d1913935d83b.gif)


**[⬆ back to top](#Vector_Clock)**



***********************************************************************************************
