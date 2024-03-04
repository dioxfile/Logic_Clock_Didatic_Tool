# Logic_Clock_Didatic_Tool

![alt text](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/QRCode_Vector_clock.png)

Code in Python to synchronize the computer clock using the [Lamport-WIKI](https://en.wikipedia.org/wiki/Leslie_Lamport) Logic Clock method. This application is used to teach Clock Synchronization in Computer Science Course subjects, for example, Distributed Systems, and it applies the concept of Lamport Logical Clocks to Physical Computer clocks and also to events occurring on these computers such as sending and receiving of messages.
## Context
People use physical time to order events. For example, we say that an event at 8:15 AM occurs before an event at 8:16 AM. In distributed systems, physical clocks are not always precise, so we can't rely on physical time to order events. Instead, we can use logical clocks to create a partial or total ordering of events. Thus, this APPLICATION explores the concept and implementation of the logical clocks invented by Leslie Lamport in his seminal paper `Time, Clocks, and the Ordering of Events in a Distributed System`, [Lamport-Paper](https://dl.acm.org/doi/10.1145/359545.359563).

# Lamport's Logic Clock Algorithm
In logical clocks, synchronization with the date/time does not need to be absolute. Furthermore, if two processes do not interact with each other, their clocks do not need to be synchronized. Thus, what happens before is taken into account, for example, two events of a process `Pi`, `a` and `b`, with `a` being the sending of a `msg` and `b` being receiving this same `msg` is equivalent to saying that `a → b`. This way, all `Processes` agree that event `a` occurs first and then event `b` occurs; 

In this context there are two situations:
* (1) `a` and `b` are from the same process, and `a` occurs before `b`, so `a → b` is true; 
* (2) `a` is the event of `msg` being sent by `P1`, and `b` is the event of the same `msg` being received by `P2`, so `a → b` is true. Furthermore, a `msg` cannot be received before it is sent. 
* The relationship between events `a → b` is transitive. Therefore, `a → b` and `b → c`, so `a → c`; 
* Event `a` has a clock `C(a)` that everyone agrees on; 
* `a → b, then C(a) < C(b)`; 
* `C` always occurs forward; 
* Time is corrected positively (`+`).  

Consequently, Lamport's algorithm is as follows:
* (Step 1) Before some event (e.g., sending to network and delivery to application) `pi executes Ci ← Ci + 1`;
* (Step 2) If `pi` sends a message `m` to `pj`, then it sets the timestamp of `m ts(m)` to equal `Ci`, after having performed `step 1`;
* (Step 3) Upon receiving `m`, `pj` adjust the local counter to `Cj ← max{Cj, ts(m)}`, after which step 1 is executed, and the message is delivered to the application; 

Therefore, each `pi` maintains a local counter `Ci`, Figure 1.
# Figure 1
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/algo.png)

1. [What are the Possible Applications?](#What-are-the-Possible-Applications)
1. [Prerequisites](#prerequisites)
1. [What do you need to use this software?](#What-do-you-need-to-use-this-software)
1. [How to install this application in your system?](#How-to-install-this-application-in-your-system)
1. [Possibles errors](#possibles-errors)
1. [How to use it?](#How-to-use-it)


</head>

# What are the Possible Applications?
Its purpose is the synchronization of physical (e.g., CMOS clock) and logical clocks of computers connected to the same network.

## Proposal Description 
In this proposal Lamport's Logical Clock Algorithm was employed to address the issue of a depleted CMOS battery, resulting in the misconfiguration of the physical clocks on computers. Consequently, when executing the application and transmitting a message across the network, the date and time of all computers linked to the network will be automatically synchronized based on the highest date and time. To achieve synchronization across the entire network, only one message is sent via broadcast or multicast. Following this, convergence occurs in less than 1 second.

## Application Operation

This application works as follows, imagine a scenario with three computers, Figure 2.
# Figure 2
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/0.png)

* In this scenario, the computer with the IP address 172.168.10.3 sends a message with its date/time via broadcast to the network (Figure 3). When computers 172.168.10.1 and 172.168.10.2 receive this message, they will behave as illustrated in Figure 4;
# Figure 3
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/1.png)

* As shown in Figure 4, the computer with the IP address 172.168.10.2 updates its local time. However, computer 172.168.10.1 does not. This occurs because the time on computer 172.168.10.1 is more up-to-date, as depicted in Figure 4;
# Figure 4
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/2.png)

* Consequently, the computer at 172.168.10.1 will broadcast a message to the network, containing the most up-to-date time. In this context, all other computers will update their times with this message. Thus, complete synchronization occurs, as depicted in Figure 5;
# Figure 5
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/3.png)

Why did we choose to return a message with the most current time via broadcast/multicast? The answer is that if we returned the message via unicast only to the message sender, the other machines that updated their times with it would not be aware that their times are outdated, as illustrated in Figure 6.
# Figure 6
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/4_.png)

# Prerequisites
* Pyhton3 (Or more)
* Python3-wxgtk4.0
* python3-pip
* ipaddr
* Python3-netifaces
* Python3-dateutil
* Python3-pubsub


# What do you need to use this software?
* You will need a GNU/Linux Ubuntu 20.04 Focal; Linux Mint 20.1 Ulyssa or other Linux system.
* And/Or Windows 10 and/or 11 Enterprise Edition.
* Internet connection for download.

Probably the software will also work on any other SO, but it has only been tested on the systems listed above.

## For x86_64 Debian-based distributions and Windows 10 and/or 11 Enterprise Edition <br/> 
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
# How to install this application in your system?
## How to install it in Debian-based Systems (x86_64)?
* Download INSTALL.sh from git<br/>
* Permit to file INSTALL.sh<br/>
  `$sudo chmod +x INSTALL.sh`

* Obs: For the above command to work, the terminal must be open where the file is located.<br/>

* Run the file<br/>
  `$sudo ./INSTALL.sh`

***********************************************************************************************
## You can do an installation automatically by running the file 'INSTALL.sh'. But if you want to install manually just follow the steps below.

* In Debian-Based Systems.

* First, you will download the package and later install it. Once the installation is finished you can delete the downloaded `*.deb` files.


1. INSTALL PYTHON3<br/>
`$sudo apt install python3`<br/>

2. INSTALE WXGTK4<br/>
`$sudo apt install python3-wxgtk4.0`<br/>

3. INSTALL IPADDR (PIP)<br/>
`$sudo apt install python3-pip`
`$sudo pip3 install ipaddr`<br/>

4. INSTALL NETIFACES<br/>
`$sudo apt install python3-netifaces`

5. INSTALL DATEUTIL<br/>
`sudo apt install python3-dateutil`<br/>

6. INSTALL PUBSUB<br/>
`sudo apt install python3-pubsub`<br/>

***********************************************************************************************

## How to install it in Windows 10 and/or 11 Enterprise Edition (x86_64)?

* On Windows 10 and/or 11 Enterprise or other versions, install "vs_BuildTools" by downloading it from the following link: https://visualstudio.microsoft.com/visual-cpp-build-tools/ <br/>
* After that, you need to run it as an administrator and check the following tools as shown in Figures 7, 8, and 9 (e.g., where the boxes are checked) <br/>
## Figure 7
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/1MS.png)
## Figure 8
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/3ms.png)
## Figure 9
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/2ms.png)
* Now click Install and wait for the installation (e.g., this may take a few minutes depending on your Internet connection) <br/>
* Now go to the Windows search bar and type PowerShell and in the PowerShell application, right-click and run as administrator as shown in Figure 10:<br/>
## Figure 10
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/4ms.png)
* At the PowerShell prompt, run the following command: `ExecutionPolicy RemoteSigned` <br/>
* If prompted, press A to confirm the action. This will set the RemoteSigned execution policy for all users <br/>
* If you want to set the execution policy for the Current User only, use the Scope parameter followed by the username. For example: `Set-ExecutionPolicy RemoteSgined -Scope CurrentUser` <br/>
* After that, download the INSTALL.ps1 script (e.g., from GitHub) and run it at the PowerShell command prompt, for example: `.\INSTALL.ps1` <br/>
* After installing python3 and all necessary libraries (e.g., wxgtk, pip, ipaddr, netifaces, dateutil, and pubsub) download the following files from git: `ds_logic_clocks_mc_30.py and varglobal.py` <br/>
* Now go to the folder where the files were downloaded and run `ds_logic_clocks_mc_30.py` as administrator (e.g., clicking it twice). <br/>

# How to use it?
## IMPORTANT: To change the computer's time you must run the application as administrator/root user.<br/>
### You just need to run the file with Python <br/>
* Linux (e.g., Bash/dash prompt) <br/>
  `$ sudo ./ds_logic_clocks_mc_30.py` <br/>
* Windows (e.g., PowerShell prompt)<br/>
  `c:\Users\Administrator> .\ds_logic_clocks_mc_30.py` <br/>
* After that, the following screen will appear (Figure 11): <br/>
## Figure 11
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/gui1.png)

**************************************************************
# Application Details: 
1 - Transmission Method, Figure 12; 
# Figure 12 
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/transmissionLC.png)
* The application can create DGRAM (UDP) IPv4 (Unicast, Multicast, and Broadcast) and IPv6 (Unicast and Multicast) sockets. A valid combination would be `Broadcast, IP Local Server - 0.0.0.0, IP Remote Server - <broadcast>, and Port 10001 (e.g., if you have a firewall this port must be open)`; 
* It is possible to use any communication port as long as another application is not already using it; 
* When clicking on the Bind IP/Port Button, for instance, the `Local Socket Assigned (Local):` panel will show the connected socket (tuple), for example: `Connection in ('0.0.0.0', 10001)`, Figure 13.
# Figure 13
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/bindLC.png) 

2 - Local Panel of Events. In the events panel, there are six types of events (Figure 14):
* (1) The one that happens in the application itself, from it to itself, and to other computers on the network. Ex: `The process at ('172.168.20.21', 52952) says, date/time: 11/08/2023 14:31:00.701633`. It shows that the local process on socket `172.168.20.21', 52952` sent the time to itself and to the network.
* (2) Return via Multicast/Broadcast/Unicast. It happens when the local process returns the most current date/time to the remote process(es) (other applications on the network). Ex: `Send R:M/B/U...` which means Multicast/Broadcast/Unicast return, depending on the transmission method used.
* (3) Update by Multicast/Broadcast/Unicast. It happens when the local application synchronizes its date/time through some remote process via a return message. Ex: `Update date/time from ('172.168.20.96', 52643) by R:M/B/U`. Figure 14.
* (4) Update by Unicast. It happens when the local application synchronizes its date/time through some remote process via the Unicast Transmission Methode. Ex: `Update date/time from ('172.168.20.96', 52683) by unicast`. 
* (5) Update by Broadcast. It happens when the local application synchronizes its date/time through some remote process via the Broadcast Transmission Methode. Ex: `Update date/time from ('172.168.20.96', 33643) by broadcast`. 
* (6) Update by Multicast. It happens when the local application synchronizes its date/time through some remote process via Multicast Transmission Methode. Ex: `Update date/time from ('172.168.20.96', 62643) by multicast`.
# Figure 14
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/panelLC.png)

3 - Hosts/Processes Panel. 
* The hosts and processes panel shows all local and remote processes (e.g., hosts) that are part of the communication for synchronization. Useful when using transmission methods such as Multicast and Broadcast, Figure 15.
# Figure 15
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/panel-processesLC.png)
* Figure 15 shows the local process, for instance, local default process/IP `0.0.0.0`, local process/IP `172.168.20.21`, and remote process/IP `172.168.20.96`.

4 - Logic Clock Panel. 
* The logical clock panel displays the number of events that occurred in the local application (e.g., Local IP), in the case of sending only messages to itself (e.g., a single application on the network) and, also, all events from remote applications which came into contact with the current process, in the case of having more than one application on the network, Figure 16. 
# Figure 16 
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/panel-LC.png)
* Figure 16 shows that the local application registered `8 events`, and the IP used for that is `0.0.0.0`. For example, if two processes pi and pj, on different nodes, exchange messages (e.g., events a and b) and if the logical clock of the sending process is 8 (eg., `Ci(a)==8`) this process will increment its clock of 1 (e.g., `Ci(a)=Ci(a+1))`, `Ci(a)==9`, and after that, it will match the time stamp of the message to be sent equal to `Ci(a)` (e.g., `tsi(mi)==Ci(a)`) and will send the message to process pj. Thus, process pj upon receiving the message will perform the following calculation: `Cj=MAX{Cj, tsi(mi)} + 1`. Therefore, if `Cj's` logical clock is equal to 5, then `Cj's` clock value will be, `Cj = MAX{5, 9} + 1 --> Cj = 10`.

5 - Local Physical Clock Display
* The Physical clock is used to show the local time configured on the computer running the application. This way, if the user changes the local time on the computer, the application will update the time instantly, Figure 17.
# Figure 17
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/phisical-LC.png)

6 - Time Difference.
* The time difference panel displays the date/time difference that was updated/synchronized in the local application and that was received from a remote application, Figure 18. 
# Figure 18
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/diffe-time-LC.png)
* Figure 18 shows that the application synchronized and that the date/time difference was: `1 hour, 2 seconds, 745 milliseconds`.

7 - RTT Ping Average Delay.
* The `RTT Ping Average` panel displays the time used to adjust the date/time received from remote processes. This method is based on [Cristian](https://www.cs.utexas.edu/users/lorenzo/corsi/cs380d/papers/Cristian.pdf).
* It works as follows:
* (1) `Local Process` requests the time from `Remote Process` at time `t0`.
* (2) The `Remote Process` after receiving the request prepare a response and append the time `T` from its own clock.
* (3) `Local Process` receives the response at time `t1` and then sets its time to be `T + RTT/2, where RTT=t1-t0`.

Therefore, to perform this calculation we use the ping program. Thus, upon receiving the updated date/time from a remote application, the current application, ' Local Process', executes the ping program in the direction of the remote application (e.g., `$ ping Remote IP`). Thus, ping returns the average `RTT` time (e.g., `rtt min/avg/max/mdev = 0.994/1.021/1.048/0.027 ms`) which is divided by two `(1.021ms/2)` and then added to the received date/time (e.g., `T + RTT/2`). That's why we call this method `RTT Ping Average`, Figure 19.
# Figure 19
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/ping-LC.png)
* Figure 19 shows the RTT value already divided by two.

8 - Send Message Methods.
* Messages can be sent automatically and manually as shown in Figure 20.
# Figure 20.
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/buttons-LC.png)
* Figure 20 shows the buttons: `Automatic Send Message`, `Stop: Automatic Message`, and `Manual Send Message`.

# Figure 21
![alt text](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/LogicClock.png)
* Figure 21 depicts the application running in the Linux System.

# Figure 22
![alt text](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/gui-win.png)
* Figure 22 depicts the application running in Windows System via VMware WorkStation 17 Player.
***********************************************************************************************

# Possibles errors

* If any module for unknown reasons has not been installed

For any module error, you may have to review the "`How to install this application in your system?`" session and manually install each module in sequence according to the tutorial. Follow all steps.<br/>

In the Debian system, you may have a user error<br/>
If you get the error "./INSTALL.sh: sudo: not found". By default, sudo is not installed, but you can install it. <br/>

First enable su-mode:<br/>
`$su`<br/>
 
Install sudo<br/>
`#apt install sudo -y`<br/>

After that, you would need to play around with users and permissions. Give sudo right to your user.<br/>
`#usermod -aG sudo username`<br/>

Edit the file 'sudoers'<br/>
`#nano /etc/sudoers`<br/>

#User privilege specification<br/>
```shellscript
root ALL=(ALL:ALL) ALL<br/>
"username" ALL=(ALL:ALL) ALL <br/><br/>
```
#The top line was the one we added. <br/>
#Replace 'username' with the name of your user who wants to have root permission<br/>
`#exit`

* update error

Obs: In some cases Debian, when new, in the updates configuration file "/etc/apt/sources.list", the line referring to the cdrom is not commented out, this causes an error at the time of the update and consequently when installing some programs and libraries with apt.
It is advisable to comment on any lines referring to the use of "cdrom" sources, and it is strongly recommended to use official Debian sources, both "Debian" and "security". Figure 23.
# Figure 23
![animation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/gif-animada.gif)

**[⬆ back to top](#Logic_Clock_Didatic_Tool)**



***********************************************************************************************
