#!/usr/bin/env bash

#####	NAME:				INSTALL
#####	VERSION:			1.4
#####	DESCRIPTION:		Install libraries and dependencies 			
#####	DATE OF CREATION:	22/01/2021
#####	WRITTEN BY:			Karan Luciano Silva
#####	E-MAIL:				karanluciano1@gmail.com			
#####	DISTRO:				Arch Linux
#####	LICENSE:			GPLv3 			
#####	PROJECT:			https://github.com/dioxfile/Vector_Clock

#root permission lockout
_checks=`id -u`
_currentuser=`whoami`

if [ $_checks != 0 ]; then
	echo “Your user is ${_currentuser}. Need be root…”
	exit 1
else

    ubuntuLTS(){
        sudo apt install -y python3-wxgtk4.0
        sudo apt install -y python3-pip
	sudo pip3 install ipaddr
        sudo apt install -y python3-netifaces
        sudo apt install -y python3-dateutil
        sudo apt install -y python3-pubsub
    }

    ubuntuLTS
    
    echo -e "\n\033[01;32mNow run the command\n# python3 ds_logic_clocks_mc_30.y\033[01;37m"
fi
