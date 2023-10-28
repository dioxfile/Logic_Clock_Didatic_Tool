# Logic_Clock_Didatic_Tool

![alt text](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/QRCode_Vector_clock.png)

Code in Python to synchronize the computer clock using the [Lamport](https://en.wikipedia.org/wiki/Leslie_Lamport) Logic Clock method.

People use the physical time to order events. For example, we say that an event at 8:15 AM occurs before an event at 8:16 AM. In distributed systems, physical clocks are not always precise, so we can't rely on physical time to order events. Instead, we can use logical clocks to create a partial or total ordering of events. This article explores the concept of and implementation of the logical clocks invented by Leslie Lamport in his seminal paper Time, Clocks, and the Ordering of Events in a Distributed System.

![alt text](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/Logic-Clock.png)
<!-- ![animacao](https://user-images.githubusercontent.com/32453979/47199699-d9c90e00-d340-11e8-94b7-6b609d44561e.gif) -->


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
* Pyhton3 (Or more)
* Python3-wxgtk4.0
* python3-pip
* ipaddr
* Python3-netifaces
* Python3-dateutil
* Python3-pubsub


# What do you need to use this software?
* You will need a GNU/Linux Ubuntu 20.04 Focal; Linux Mint 20.1 Ulyssa .
* Internet connection for download.

Probably the software will also work on any other Ubuntu-based, but it has only been tested on the systems listed above.


* For x86_64 Ubuntu-based distributions<br/> 
These are the necessary packages and modules.
The version may not necessarily be the same, but these versions have been tested and confirmed the operation.

* 1. PYTHON3 <br/>
Package: python3 <br/>
Version: 3.8.2-0ubuntu2 <br/>

* 2. WXGTK4<br/>
Package: python3-wxgtk4.0<br/>
Version: 4.0.7+dfsg-2build1 <br/>

* 3. PIP-3<br/>
Package: python3-pip<br/>
Version: 22.0.2<br/>

* 4. IPADDR<br/>
Package: ipaddr<br/>
Version: 2.2.0<br/>

* 5. NETIFACES<br/>
Package: python3-netifaces<br/>
Version: 0.10.4-1ubuntu4<br/>

* 6. DATEUTIL<br/>
Package: python3-dateutil<br/>
Version: 2.7.3-3ubuntu1<br/>

* 7. PUBSUB<br/>
Package: python3-pubsub<br/>
Version: 4.0.3-4<br/>


***********************************************************************************************
# How to install it?

* For x86_64<br/>
Give permission to file INSTALL.sh<br/>
`$sudo chmod +x INSTALL.sh`

Obs: For the above command to work the terminal must be open where the file is located.<br/>

Run the file<br/>
`$sudo ./INSTALL.sh`

***********************************************************************************************
* You can do an installation automatically by running the file 'INSTALL.sh'. But if you want to install manually just follow the steps below.

* In Ubuntu and Mint.

First you will download the package and later install it.

Once the installations are finished you can delete the downloaded .deb files.


1. INSTALL PYTHON3<br/>
`$sudo apt install python3`<br/>

2. INSTALE WXGTK4<br/>
`$sudo apt install python3-wxgtk4.0`<br/>

3. INSTALL IPADDR (PIP)<br/>
`$sudo apt install python3-pip`
`$sudo pip3 install ipaddr`<br/>


5. DOWNLOAD NETIFACES<br/>
`$sudo apt install python3-netifaces`

6. INSTALL IPADDR<br/>
`$sudo apt install python-ipaddr`<br/>

7. INSTALL DATEUTIL<br/>
`sudo apt install python3-dateutil`<br/>

8. DOWNLOAD PUBSUB<br/>
`sudo apt install python3-pubsub`<br/>

***********************************************************************************************

# How to use it?

*  IMPORTANT: For the hours to change you must have root permission or be the root user.<br/>

You just need to run the file with python

`$ sudo python3 ds_logic_clocks_mc_30.py`
**************************************************************

The simplest way to use eh the "Broadcast"<br/>

* 1 - Shows the time that is "wrong"<br/>

* 2 - Click "Bind IP/Port" to make a connection<br/>

* 3 - You can choose between automatic and manual<br/>
Automatic: Send a message every 3 seconds<br/>
Manual: Send a message each time you click on it<br/>

* 4 - Note that the time has changed, important to realize that it has changed to an hour higher than it was already. Your time is now synchronized.<br/>

<!-- ![animacao](https://user-images.githubusercontent.com/32777186/47819566-48d73700-dd31-11e8-87e7-d1913935d83b.gif) -->

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

**[⬆ back to top](#Vector_Clock)**



***********************************************************************************************
