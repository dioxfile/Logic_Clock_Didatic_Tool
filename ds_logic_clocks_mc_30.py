#!/usr/bin/python3
#File: ds_logic_clocks_mc.py

"""**************************************************************************
  *   Name: "Socket Logic Clock's". This software synchronizes       *
  *   physical clocks using the concept of Lamport logical clocks.          *
  *                                                                         *
  *   Copyright (C) 2016 by Diogenes Antonio Marque Jose and Bruno Hernandes*
  *   dioxfile@unemat.br and hernandes.bruno@unemat.br                      *
  *   UNEMAT Brazil, Barra do Bugres Campus: bbg.unemat.br.                 *
  *                                                                         *
  *   This program is free software; you can redistribute it and/or modify  *
  *   it under the terms of the GNU General Public License as published by  *
  *   the Free Software Foundation; either version 3 of the License, or     *
  *   (at your option) any later version.                                   *
  *                                                                         *
  *   This program is distributed in the hope that it will be useful,       *
  *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
  *   MERCHANTABILITY or FITNESS FOR A IPICULAR PURPOSE.  See the           *
  *   GNU General Public License for more details.                          *
  *                                                                         *
  *   You should have received a copy of the GNU General Public License     *
  *   along with this program; If not, see <http://www.gnu.org/licenses/>.  * 
  **************************************************************************"""
import wx, subprocess # GUI Widgets and record command in var
import wx.lib.scrolledpanel as scrolled
import socket, os, sys, struct # IPC: socket; Command date Linux: to alter date/time and error sys; and convert string to packet
from datetime import datetime, timedelta # Basic date and time types
from time import gmtime, strftime # Format date type 
import time #To use in Countdown Class
import threading # Threads in python: to create server thread
import wx.gizmos as gizmos # Led Display date/time
#from wx.lib.pubsub import publisher #Write information from any class to other
#from wx.lib.pubsub import Publisher #as publisher #Write information from any class to other
#from wx.lib.pubsub import pub as Publisher
from pubsub import pub as Publisher
import varglobal # Global var shared between class
from socket import error as socket_error #error socket
from dateutil import parser
import netifaces, ipaddr #catch the ip default gateway an apply mask to IP Address
import platform #ADD by hernandes.bruno@unemat.br 
import locale #ADD by hernandes.bruno@unemat.br 
import re #ADD by hernandes.bruno@unemat.br
import ast
#Global Vars
MAX_BYTES = 65535
#=== Countdown Thread: it allows to send a message each three seconds ===
"""Based on: https://goo.gl/vLDlOs"""
class CountDown(threading.Thread):
    def __init__(self, parent):
        """Starting CountDown"""
        threading.Thread.__init__(self)
        self._parent = parent
        self._stopevent = threading.Event()
        self._sleepperiod = 3.0
        try:
            wx.CallAfter(Publisher.sendMessage, "main_event", message="\n\nAutomatic Send MSG Activated!!!"+"\n\n")
        except SomeError as msg:
            wx.CallAfter(Publisher.sendMessage, "main_event", message="SYS ERROR!!!"+str(msg)+"\n")
            
    #----------------------------------------------------------------------
    #Code to be executed in this thread
    def run(self):
        while not self._stopevent.isSet():
            self.run_c()
            self._stopevent.wait(self._sleepperiod)

    #-------------------------------------------------------------------------
    #Wait a thread finish 
    def join(self, timeout=None):
        """ Stop this thread. """
        self._stopevent.set()
        threading.Thread.join(self, timeout)

    #-------------------------------------------------------------------------
    #client used by class thread CountDown to send a message each three seconds 
    def run_c(self):
       #IP
       a = MyPanel.ip_classe #Server Me
       uni = MyPanel.ip_unicast 
       #Port Server
       j = MyPanel.porta_classe #Port
       IP_3 = uni
       try:
            """Client level three"""
            addrinfo = socket.getaddrinfo(a, None)[0]
            #Create a SOcket UDP and assign local IP
            self.client3 = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
            #Time-to-live
            ttl = struct.pack('@i', 8) # LANs ttl < 32, and MAN, WAN, etc, ttl > 32.
            if addrinfo[0] == socket.AF_INET: # IPv4
                if MyPanel.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    #Send a message by multicast
                    self.client3.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
                elif MyPanel.CHOOSE_T_METHOD == "Broadcast": #BROADCAST
                    #Send a message by broadcast
                    self.client3.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    IP_3 = uni.lower()
                else: #UNICAST
                    IP_3 = uni
            else: # IPv6 
                if MyPanel.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    self.client3.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl)
                else: #UNICAST
                    IP_3 = uni
                    
            #Take local date/time and send to others processes
            data_a = datetime.now()
            #format date/time
            self.texto3 = data_a.strftime("%m/%d/%Y %H:%M:%S.%f")
            #coding date/time
            message = self.texto3.encode('ascii')+b" Normal" 
            #Count and log transmission event -> Step one Lamport Algorithm
            varglobal.soma += 1
            #Step two Lamport Algorithm
            message += b" "+str(varglobal.soma).encode('ascii')
            #sending date/time to others process
            self.client3.sendto(message,(IP_3, j))
            if MyPanel.CHOOSE_T_METHOD == "Unicast" or a == netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr']:
                self.client3.sendto(message,(a, j))                
       except socket.error as msg:
           self.textDisplay.write("SOCKET ERROR (C3), "+str(msg)+"\n")
           #sys.exit()


#=== Server Thread: make capable run distinct instances of server===
class Socket_RL(threading.Thread):
    """Server Thread"""
    #-------------------------------------------------------------------
    #Start Thread
    def __init__(self, parent):
        """Starting Server"""
        threading.Thread.__init__(self)
        self._parent = parent
        self._stopevent = threading.Event()
        self.a = MyPanel.ip_classe #Local Server
        self.b = MyPanel.porta_classe
        self.uni = MyPanel.ip_unicast #Send message to this IP
        try:
            addrinfo = socket.getaddrinfo(self.a, None)[0]
            self.sock = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
            #UDP socket Bind
            self.sock.bind((self.a,self.b))
            #IPv4 or IPv6, group type
            group_type = socket.inet_pton(addrinfo[0], addrinfo[4][0])
            # Join to the group
            if addrinfo[0] == socket.AF_INET: # IPv4
                if MyPanel.CHOOSE_T_METHOD == "Multicast":
                    mreq = group_type + struct.pack('=I', socket.INADDR_ANY)
                    self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
            else: # IPv6
                if MyPanel.CHOOSE_T_METHOD == "Multicast":
                    mreq = group_type + struct.pack('@I', 0)
                    self.sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)
            #Publisher Event Warning in Panel received MS 
            wx.CallAfter(Publisher.sendMessage, "sock_connect", message="Connection in {}".format(self.sock.getsockname()))
        except socket.error as msg:
            self.sock.close()
            wx.CallAfter(Publisher.sendMessage, "main_event", message="SOCKET ERROR, "+str(msg)+"\n")
            
    #-------------------------------------------------------------------
    #cacth only IP to comparison
    def catch_ip(self, ip):
        ip_ = str(ip)
        if ip_ == "":
            ip_ = "('0.0.0.0', TEST)"
        lista = ip_.split("'")
        return lista[1]

    #-------------------------------------------------------------------
    #catch R:M/B
    def catch_rb(self,rb):
        rb_ = str(rb)
        lista = rb_.split(" ")
        return lista[2]

    #-------------------------------------------------------------------
    #catch Vector Value of remote process
    def catch_vv(self,vv):
        vv_ = str(vv)
        lista = vv_.split(" ")
        return lista[3]
    
    #-------------------------------------------------------------------
    #catch only date/time
    def only_dt(self,dt):
        dt_ = str(dt)
        lista = dt_.split(" ")
        return lista[0]+" "+lista[1]

    #-------------------------------------------------------------------
    #RTT calc to measure delay, based average PING rtt
    #-------------------------------------------------------------------
    def rtt(self, ip):
        system = platform.system()
        ip_ = str(ip[0])
        output = 0.0
        if ":" in ip_:
            if system == "Windows":
                command= f'ping -6 -n 1 {ip_}'
            else: 
                command = f'ping6 -c 1 {ip_} | egrep rtt | awk -F\"/\" \'{{print $5}}\''
        else:
            if system == "Windows":
                command = f'ping -n 1 {ip_}'
            else:
                command = f'ping -c 1 {ip_} | egrep rtt | awk -F\"/\" \'{{print $5}}\''         
        output = subprocess.getoutput(command)
        if system == "Windows":
            match = re.search(r"Média = (\d+)ms", output)
            if match:
                ms_win = float(match.group(1)) / 1000.0
                output = ms_win
            else:
                output = 0.0005
        else:
            ms_linux = float(output) / 1000.0
            output = ms_linux
        if output == "":
            output= 0.00001
        return output        
        
    #-------------------------------------------------------------------
    #Tests whether the IP is a valid IPv4/IPv6
    #-------------------------------------------------------------------
    def validate_ip_address(self, ip_string):
        msg = "000"
        try:
            ip_object = ipaddr.IPv4Address(ip_string)
            msg = "True"
        except ValueError:
            msg = "False"
        finally:
            return msg
    #-------------------------------------------------------------------
            
    #Thread called by main Thread
    def run(self):
        """Run "server" """        
        #Dictionary to IP list and vector value of remote process
        v = {}
        C_i = {}
        while True:
            try:
                "Server Level One"
		#Receive from Client
                self.data, self.address = self.sock.recvfrom(MAX_BYTES)
                #decode date/time, received from client, to ascii
                self.text = self.data.decode('ascii')
                #Publisher Event Warning in Panel received MSG
                wx.CallAfter(Publisher.sendMessage, "main_event", message="The process at {} says, date/time: {}".format(self.address, self.only_dt(self.text))+"\n")
                
                """Logic clock algorithm""" 
                ############################
                C_i.setdefault(self.a, [])
                l=self.catch_vv(self.data).split("'") #"""New Change for Python3"""
                C_i[self.a].append(int(l[0]))
                self.ord_lv = list()
                for k,val in list(C_i.items()):
                    self.ord_lv.append((k,max(val)))
                self.ord_lv.sort()
                wx.CallAfter(Publisher.sendMessage, "logic", message=str(self.ord_lv)+"\n")             
                
                #Receive event internal count -> Step three Lamport Algorithm
                """Logic clock algorithm""" 
                ############################
                if str(self.validate_ip_address(self.catch_ip(self.address)))=="False":
                    IP_LOCAL=netifaces.ifaddresses(netifaces.gateways()[2][0][1])[10][0]['addr']
                else:
                    IP_LOCAL=netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr']		
                interPip = self.catch_ip(self.address)
                elem = str(interPip)
                #Tests whether the IP is Remote or Local
                if IP_LOCAL != self.catch_ip(self.address):
                    vector = int(l[0]) #"""New Change for Python3"""               
                    varglobal.soma = max(varglobal.soma, vector)+1
                    wx.CallAfter(Publisher.sendMessage, "logic", message=str(self.ord_lv)+"\n")
                else:
                    vector = int(varglobal.soma)
                wx.CallAfter(Publisher.sendMessage, "logic", message=str(self.ord_lv)+"\n")
                v.setdefault(interPip, [])
                v[interPip].append(vector)
                v.setdefault(self.a, [])
                v[self.a].append(varglobal.soma)
                self.ord_v = list()
                #Remove element when remote process close
                if self.catch_rb(self.text) == "CLOSE":
                    try:
                        del v[elem]
                        wx.CallAfter(Publisher.sendMessage, "main_event", message="\n\n Remote {}".format(self.address)+" process closed (T). \n\n")
                    except KeyError:
                        wx.CallAfter(Publisher.sendMessage, "main_event", message="\n\n Remote {}".format(self.address)+" process closed (E). \n\n")
                for k,val in list(v.items()):
                    self.ord_v.append((k))
               
                self.ord_v.sort()                                    
                wx.CallAfter(Publisher.sendMessage, "vector", message=str(self.ord_v)+"\n")
                ################################
                """End vector clock algorithm"""
                
                #Catch lacal date/time
                data_local = datetime.now()
                #Extract IP from remote socket
                self.from_ = self.catch_ip(self.address)
                #Catch socket from local client
                Sck = MyPanel.S_local
                #Extract IP from local socket (client)
                self.local_ = self.catch_ip(Sck)
                #Extract IP from local socket (server)
                self.local_sock = self.catch_ip(self.sock.getsockname())
                #Convert remote date/time string to datetime.datetime format 
                remote_date_ = parser.parse(self.only_dt(self.text))
                #Test if msg arrived from remote client
                if (self.from_ != self.local_) and (self.from_ != self.local_sock) and (self.from_ != self.a):
                    #Comparison local date/time and remote date/time
                    self.LOCAL = float(((time.mktime(data_local.timetuple())*1000)/1000)/1000)
                    self.REMOTE = float(((time.mktime(remote_date_.timetuple())*1000)/1000)/1000)                                      
                    
                    if self.LOCAL < self.REMOTE:
                        difference = abs(remote_date_ - data_local)
                        time_list = [
                            (difference.days // 365, "year"),
                            ((difference.days % 365) // 30, "month"),
                            ((difference.days % 365) % 30, "day"),
                            (difference.seconds // 3600, "hour"),
                            ((difference.seconds % 3600) // 60, "minute"),
                            (difference.seconds % 60, "second"),
                            (difference.microseconds // 1000, "millisecond")]
                        time_units = []
                        for value, unit in time_list:
                            if value > 0:
                                if value > 1:
                                    unit += "s"
                                time_units.append(f"{value} {unit}")
                        diff_time= ", ".join(time_units)
                        wx.CallAfter(Publisher.sendMessage, "time", message=str.format((diff_time)))
                        #PING RTT Method (By Diogenes)
                        OLD_H = datetime.now()
                        
                        # Approximate Time of Propagation (ATP), based average PING RTT
                        ATP = float(self.rtt(self.address))
                        NOW_H = datetime.now()
                        time_diff= OLD_H - NOW_H
                        delay= abs(time_diff.total_seconds())
                        RTT = delay+(float(ATP)/2)
                        AUX_RTT = RTT * 1000
                        #New hour to setup in system
                        self.h = (time.mktime(remote_date_.timetuple())*1000 + \
                                  (int(remote_date_.strftime('%f'))+AUX_RTT)/1000)/1000
                        wx.CallAfter(Publisher.sendMessage, "rtt", message="{:.5f}".format((RTT)))                        
                        #Set remote date/time in this server
                        system_language= locale.getdefaultlocale()[0]
                        system= platform.system()
                        if system == "Windows":
                            if system_language.lower() == "en_us":
                                date_time_win= datetime.fromtimestamp(self.h).strftime("%m/%d/%y %H:%M:%S")
                            else:
                                date_time_win= datetime.fromtimestamp(self.h).strftime("%d/%m/%y %H:%M:%S")
                            os.system(f'date {date_time_win.split()[0]} & time {date_time_win.split()[1]}')
                        else:
                            if system_language.lower() == "en_us":
                                os.system('date -s "{}"'.format(datetime.fromtimestamp(self.h).strftime("%m/%d/%Y %H:%M:%S.%f")))
                            else:
                                os.system('date -s "{}"'.format(datetime.fromtimestamp(self.h).strftime("%d/%m/%Y %H:%M:%S.%f")))
                        #End of amendment II ------------------------------------------------------
                        #Check if MSG arrived from R:M/B/U (Reply by Multicast/Broadcast/Unicast)
                        if self.catch_rb(self.text) == "R:M/B/U":
                            #Publisher Event Warning in Panel received MS by R:M/B/U
                            wx.CallAfter(Publisher.sendMessage, "main_event", message="Update date/time from {}".format(self.address)+" by R:M/B/U.\n")
                        elif MyPanel.CHOOSE_T_METHOD == "Multicast":
                            #Publisher Event Warning in Panel received MS by MULTICAST
                            wx.CallAfter(Publisher.sendMessage, "main_event", message="Update date/time from {}".format(self.address)+" by multicast.\n")
                        elif MyPanel.CHOOSE_T_METHOD == "Broadcast":
                            #Publisher Event Warning in Panel received MS by BROADCAST
                            wx.CallAfter(Publisher.sendMessage, "main_event", message="Update date/time from {}".format(self.address)+" by broadcast.\n")
                        else:
                            #Publisher Event Warning in Panel received MS by UNICAST
                            wx.CallAfter(Publisher.sendMessage, "main_event", message="Update date/time from {}".format(self.address)+" by unicast.\n")
                    #Comparison local date/time and remote date/time
                    elif self.LOCAL > self.REMOTE:
                        #Send MSG
                        self.exec_client()
                    else:
                        #Publisher Event Warning in Panel received MS
                        wx.CallAfter(Publisher.sendMessage, "vector", message=str(self.ord_v)+"\n")
                        wx.CallAfter(Publisher.sendMessage, "logic", message=str(self.ord_lv)+"\n")
                    
            except socket.error as msg:
                #Publisher Event Warning in Panel received MS
                wx.CallAfter(Publisher.sendMessage, "main_event", message="RECEIVING ERROR (S), "+str(msg)+"\n")

    #-------------------------------------------------------------------
    #Client called by main Thread to send R:M/B message
    def exec_client(self):
        """EXC_Client level Two"""
        IP_2=self.a #Server, me
        try:
            addrinfo = socket.getaddrinfo(self.a, None)[0]
            #Create a SOcket UDP and assign local IP
            self.cli = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
            #Time-to-live
            ttl = struct.pack('@i', 8) # LANs ttl < 32, and MAN, WAN, etc, ttl > 32.
            if addrinfo[0] == socket.AF_INET: # IPv4
                if MyPanel.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    #Send a message by multicast
                    self.cli.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
                elif MyPanel.CHOOSE_T_METHOD == "Broadcast": #BROADCAST
                    #Send a message by broadcast
                    self.cli.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    IP_2 = self.uni.lower()
                else: #UNICAST
                    IP_2 = self.uni
            else: # IPv6 
                if MyPanel.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    self.cli.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl)
                else: #UNICAST
                    IP_2 = self.uni

            #Catch new date/time (updated)
            self.tex = datetime.now()
            self.d_time = self.tex.strftime("%m/%d/%Y %H:%M:%S.%f")
            messag = self.d_time.encode('ascii')+b" R:M/B/U"
            #Count and log transmission event -> Step one Lamport Algorithm
            varglobal.soma +=1
            messag += b" "+str(varglobal.soma).encode("ascii")
            self.cli.sendto(messag,(IP_2, self.b))
            if MyPanel.CHOOSE_T_METHOD == "Unicast" or self.a == netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr']:
                self.cli.sendto(messag,(self.a, self.b))
            #Publisher Event Warning in Panel received MS
            wx.CallAfter(Publisher.sendMessage, "main_event", message="Send R:M/B/U..."+"\n")
        except socket.error as msg:
             #Publisher Event Warning in Panel received MS
             wx.CallAfter(Publisher.sendMessage, "main_event", message="SENDING ERROR (S), "+str(msg)+"\n")
    
#========== GUI: Create the Window with differents Widgets =============
#======== Main Window : displays the main window to the user ===========
class MyPanel(wx.Frame):
    """Graphic User Interface WX.FRAME"""
    #Class's Global Vars
    ip_classe = ""
    porta_classe = 0
    S_local = ""
    CHOOSE_T_METHOD = ""
    CHOOSE_D_METHOD = ""
    ip_unicast = ""
    CLOSE = ""

    #----------------------------------------------------------------------
    #Main function GUI
    def __init__(self, parent, id=-1,title="Socket Logic Clock's - DS",pos=wx.DefaultPosition,
         size=(795,700), style=wx.DEFAULT_FRAME_STYLE):
        """Constructor"""
        wx.Frame.__init__(self,parent,id,title,pos,size,style)
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(1, 1, 795, 700)
        self.panel = wx.Panel(self.scroll,wx.ID_ANY)
        self.Bind(wx.EVT_CLOSE, self.OnExitApp)
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusText('Developed by Diogenes Antonio M. Jose UNEMAT Brazil.')
        self.statusbar.SetStatusText('Computer Science - Distributed Systems.', 1)
        self.Center()
        #-------------------------------------#
        #Permit choose transmission method
        list_Method = ['Broadcast','Multicast','Unicast'] 	  
        self.rbox = wx.RadioBox(self.scroll, label = 'Transmission Method', pos=(5,20), choices = list_Method,
        majorDimension = 1, style = wx.RA_SPECIFY_ROWS) 
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onSelect_RadioBox)
        MyPanel.CHOOSE_T_METHOD = self.rbox.GetStringSelection()
        #self.rbox.EnableItem(0, enable=False)
        #self.rbox.ShowItem(0, show=True)
        #print self.rbox.ShowItem(0, show=False)
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Type a IP to the Server: ", size=(200,20), pos=(5, 70))
        self.i = wx.TextCtrl(self.scroll, -1, "0.0.0.0", size=(250,30), pos=(195,70))
        self.i.SetBackgroundColour("gray")
        self.i.SetForegroundColour("white")
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Type a IP to send a message: ", size=(280,20), pos=(5, 105))
        self.c = wx.TextCtrl(self.scroll, -1, "<broadcast>", size=(250,30), pos=(195,105))
        self.c.SetBackgroundColour("gray")
        self.c.SetForegroundColour("white")
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Type a Port to the Server: ", size=(250,20), pos=(5,140))
        self.p = wx.TextCtrl(self.scroll, -1, "9093",  size=(100,30), pos=(195,140))
        self.p.SetBackgroundColour("gray")
        self.p.SetForegroundColour("white")
        #-------------------------------------#
        self.Press = wx.Button(self.scroll, -1, "Bind IP/Port", size=(150,40), pos=(5,183))
        self.Press.Bind(wx.EVT_BUTTON, self.start_Thread, id = self.Press.GetId())
        #Receiver Publisher
        Publisher.subscribe(self.updateSockConnect, "sock_connect")
        #-------------------------------------#
        self.Press_u = wx.Button(self.scroll, -1, "Close Application", size=(150,40), pos=(185,183))
        self.Press_u.Bind(wx.EVT_BUTTON, self.close_socket)
        #Receiver Publisher
        Publisher.subscribe(self.updateSockConnect, "sock_connect")
        #-------------------------------------#
    	#Date Time LED Display
        """Based on:  https://goo.gl/U4gHzg"""
        self.led = gizmos.LEDNumberCtrl(self.scroll, -1, pos=(335,12), size=(450,45))
        #Default colours
        self.led.SetBackgroundColour("black")
        self.led.SetForegroundColour("red")
        self.ActiveTimer(None)
        self.timer = wx.Timer(self, -1)
        #Update clock digits every second (1000ms)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.ActiveTimer)
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Local Socket Assigned (Local): ", size=(200,20), pos=(5,225))
        self.textarea_s = wx.TextCtrl(self.scroll, -1, "DISCONNECTED!!!",style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY| wx.TE_RICH2,
        size=(350,50), pos=(5,245))
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.textarea_s.SetForegroundColour("red")
        self.textarea_s.SetFont(font)
        self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        self.ip_srv = self.textarea_s
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Local Events Panel: ", size=(200,20), pos=(5,300))
        self.textDisplay = wx.TextCtrl(self.scroll, -1, style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY| wx.TE_RICH2, 
	size=(500,300), pos=(5,320))
        #Receiver Publisher
        Publisher.subscribe(self.updatePanelEvent, "main_event")
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "RTT Ping Average:", size=(150,20), pos=(620,122))
        wx.StaticText(self.scroll, -1, "Delay (sec)", size=(100,20), pos=(620,140))
        self.texRtt = wx.TextCtrl(self.scroll, -1, "No Delay...", style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY| wx.TE_RICH2, 
	size=(90,18), pos=(690,140))
        self.texRtt.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        #Receiver Publisher
        Publisher.subscribe(self.rtt_, "rtt")
        #Time difference--------------------------------------------------
        wx.StaticText(self.scroll, -1, "Time Differnce:", size=(150,20), pos=(620,65))
        self.texDtime = wx.TextCtrl(self.scroll, -1, "None", style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY| wx.TE_RICH2, 
	size=(160,37), pos=(620,80))
        self.texDtime.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        Publisher.subscribe(self.diff_time, "time")
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Hosts/Proccess Panel: ", size=(200,20), pos=(400,140))
        self.textVC = wx.TextCtrl(self.scroll, -1, style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY| wx.TE_RICH2, 
	size=(380,150), pos=(400,160))
        self.textVC.SetDefaultStyle(wx.TextAttr(wx.BLUE))
        #Receiver Publisher
        Publisher.subscribe(self.updateVector, "vector")
        #-------------------------------------#
        wx.StaticText(self.scroll, -1, "Logic Clock Panel: ", size=(200,20), pos=(510,320))
        self.textLC = wx.TextCtrl(self.scroll, -1, style=wx.TE_MULTILINE|wx.BORDER_SUNKEN|wx.TE_READONLY| wx.TE_RICH2, 
	size=(270,100), pos=(510,340))
        self.textLC.SetDefaultStyle(wx.TextAttr(wx.RED))
        #Receiver Publisher
        Publisher.subscribe(self.updateLogic, "logic")
        #-------------------------------------#
        self.countD = wx.Button(self.scroll, -1, label="Automatic Send Message", size=(200,30), pos=(520,470))
        self.countD.Bind(wx.EVT_BUTTON, self.Tcount)
        #-------------------------------------#
        self.stop = wx.Button(self.scroll, -1, label="Stop: Automatic Message", size=(200,30), pos=(520,530))
        self.stop.Bind(wx.EVT_BUTTON, self.stopT)
        #-------------------------------------#
        self.btn = wx.Button(self.scroll, -1, label="Manual Send Message", size=(200,30), pos=(520,590))
        self.btn.Bind(wx.EVT_BUTTON, self.run_client)

    #------------------------------------------------------------------------------------------------------------------------
    #Verify Message send method, IP version: Unicast, Broadcast or Multcast, and IPv4 or IPv6 protocol, and Delay Calculation.
    def Info(parent, message, caption = 'Information!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    #----------------------------------------------------------------------
    def Warn(parent, message, caption = 'Warning!'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()

    #----------------------------------------------------------------------
    #Catch Transmission method
    def onSelect_RadioBox(self,e):
        MyPanel.CHOOSE_T_METHOD = self.rbox.GetStringSelection()
        
    #----------------------------------------------------------------------
    #Start Thread_Count
    def Tcount(self,evt):
        self.b = CountDown(self)
        self.b.deamon=True
        self.b.start()
        self.countD.Enable(False)
        self.btn.Enable(False)
        self.stop.Enable(True)

    #----------------------------------------------------------------------
    #Stop Thread_Count
    def stopT(self,evt):
        self.countD.Enable(True)
        self.btn.Enable(True)
        self.stop.Enable(False)
        self.b.join()
        self.textDisplay.write("\n\nAutomatic Send MSG Stopped!!!"+"\n\n")
        
    #----------------------------------------------------------------------
    #Update Display Bind Socket
    def updateSockConnect(self, message):
        """
        Catch data from thread and updates the display
        """
        self.textarea_s.write(message)

    #----------------------------------------------------------------------
    #Update Display of Main Panel
    def updatePanelEvent(self, message):
        """
        Catch data from thread and updates the main event display
        """
        m = message
        s = m.split("'")
        if m != "Send R:M/B/U..."+"\n":
            if s[0] == "The process at (":
                self.textDisplay.SetDefaultStyle(wx.TextAttr(wx.BLUE))
            else:
                self.textDisplay.SetDefaultStyle(wx.TextAttr(wx.RED))
            self.textDisplay.write(m)
        elif m == "Send R:M/B/U..."+"\n":
            self.textDisplay.SetDefaultStyle(wx.TextAttr(wx.BLACK))
            self.textDisplay.write(m)
        else:
            self.textDisplay.SetDefaultStyle(wx.TextAttr(wx.BLUE))
            self.textDisplay.write(m)
            
    #----------------------------------------------------------------------
    #Update Display of Vector Panel 
    def updateVector(self, message):
        """
        Catch data from thread and updates the vector event display
        """
        self.textVC.Clear()
        self.textVC.write(message)

    #----------------------------------------------------------------------
    #Update Display of Logic Clock Panel 
    def updateLogic(self, message):
        """
        Catch data from thread and updates the logic clock event display
        """
        self.textLC.Clear()
        string = message
        SK = ast.literal_eval(string)
        if int(SK[0][1]) < int(varglobal.soma):
            self.textLC.write("[('"+SK[0][0]+"', "+str(varglobal.soma)+")]")
        else:
            self.textLC.write(message)

    #----------------------------------------------------------------------
    #Update RTT Display 
    def rtt_(self, message):
        """
        Catch rtt from thread and updates the rtt display
        """
        self.texRtt.Clear()
        self.texRtt.write(message)
        
    #Update Diff Time Display
    def diff_time(self, message):
        """
        Catch diff time and updates the display
        """
        self.texDtime.Clear()
        self.texDtime.write(message)       
    #-------------------------------------------------------------------
    #Show date/time on LED Display
    """Based on:  https://goo.gl/U4gHzg"""
    def ActiveTimer(self, event):
        #Catch current date_time from system
        date_time = datetime.now()
        DT = date_time.strftime("%m-%d-%Y %H:%M:%S")
        str(self.led.SetValue(DT))

    #-------------------------------------------------------------------
    # Start Main Thread and load vars IPs:Port end Validate Fields
    def start_Thread(self, event):
        addrinfo = ""
        IP_ = ""
        IP = ""
        
        try:
            addrinfo = socket.getaddrinfo(str(self.i.GetValue().lower()), None)[0]
            IP_ = str(self.i.GetValue()).split(':')
            IP = IP_[0]
            
            if not self.i.GetValue() or not self.c.GetValue() or not self.p.GetValue():
                self.Warn("The IP and port fields can not be empty!!!")            

            elif MyPanel.CHOOSE_T_METHOD == "Broadcast":
                if self.c.GetValue().lower() == "<broadcast>" and addrinfo[0] == socket.AF_INET and \
                   (self.i.GetValue().lower() == netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr'] or \
                      self.i.GetValue().lower() == "0.0.0.0"):
                    self.ip_ = str(self.i.GetValue().lower())
                    self.c_ = str(self.c.GetValue().lower()) 
                    self.porta_ = int(self.p.GetValue())
                    MyPanel.ip_classe = self.ip_
                    MyPanel.porta_classe = self.porta_
                    MyPanel.ip_unicast = self.c_
                    self.s = Socket_RL(self)
                    self.s.daemon = True
                    self.s.start()
                    self.countD.Enable(True)
                    self.btn.Enable(True)
                    self.Press.Disable()
                    self.rbox.Enable(False)
                    self.Press_u.Enable(True)
                    self.textarea_s.Clear()
                    self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))

                elif self.c.GetValue().lower() == netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['broadcast'] and \
                     addrinfo[0] == socket.AF_INET and \
                   (self.i.GetValue().lower() == netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr'] or \
                      self.i.GetValue().lower() == "0.0.0.0"):
                    self.ip_ = str(self.i.GetValue().lower())
                    self.c_ = str(self.c.GetValue().lower()) 
                    self.porta_ = int(self.p.GetValue())
                    MyPanel.ip_classe = self.ip_
                    MyPanel.porta_classe = self.porta_
                    MyPanel.ip_unicast = self.c_
                    self.s = Socket_RL(self)
                    self.s.deamon=True
                    self.s.start()
                    self.countD.Enable(True)
                    self.btn.Enable(True)
                    self.Press.Disable()
                    self.rbox.Enable(False)
                    self.Press_u.Enable(True)
                    self.textarea_s.Clear()
                    self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))

                else:
                    self.Warn("Warning! The client or server address is not \
compatible with the sending method or IP not configured!!!")
                    
            elif MyPanel.CHOOSE_T_METHOD == "Multicast":
                c_ip = self.c.GetValue().lower()
                if c_ip == '<broadcast>':
                    c_ip = '0.0.0.0'
                if addrinfo[0] == socket.AF_INET:
                    if ipaddr.IPv4Address(str(self.i.GetValue().lower())).is_multicast == False \
                                          or ipaddr.IPv4Address(str(c_ip)).is_multicast == False \
                                          or (ipaddr.IPv4Address(str(c_ip)) != \
                                          ipaddr.IPv4Address(str(self.i.GetValue().lower()))):
                        self.Warn("Warning! This IP is not a multicast and/or server IP address is different \
from the client IP address!!!")
                    elif str(self.i.GetValue().lower()) == '224.0.0.1':
                        self.Warn("Warning! All hosts and multicast groups assigned to this address will receive \
packets, making it unsuitable for testing purposes!!!")
                    else:
                        self.ip_ = str(self.i.GetValue().lower())
                        self.c_ = str(self.c.GetValue().lower()) 
                        self.porta_ = int(self.p.GetValue())
                        MyPanel.ip_classe = self.ip_
                        MyPanel.porta_classe = self.porta_
                        MyPanel.ip_unicast = self.c_
                        self.s = Socket_RL(self)
                        self.s.deamon=True
                        self.s.start()
                        self.countD.Enable(True)
                        self.btn.Enable(True)
                        self.Press.Disable()
                        self.rbox.Enable(False)
                        self.Press_u.Enable(True)
                        self.textarea_s.Clear()
                        self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))
                else:
                    c_ip6 = self.c.GetValue().lower()
                    if c_ip6 == '<broadcast>':
                        c_ip6 = '::'
                    if ipaddr.IPv6Address(str(self.i.GetValue().lower())).is_multicast == False  \
                                          or ipaddr.IPv6Address(str(c_ip6)).is_multicast == False \
                                          or (ipaddr.IPv6Address(str(c_ip6)) != \
                                          ipaddr.IPv6Address(str(self.i.GetValue().lower()))):
                        self.Warn("Warning! This IPv6 is not a multicast and/or server IP address is different \
from the client IP address!!!")
                    elif (IP[3:4] == "0" or IP[3:4] == "1" or IP[3:4] == "2"):
                        self.Warn("Warning! Multicast IPv6 invalid. Please consult \
IPv6 Multicast Address Space Registry in: 'https://goo.gl/oKGRno' or try ff03::1!!!")
                    else:
                        self.ip_ = str(self.i.GetValue().lower())
                        self.c_ = str(self.c.GetValue().lower()) 
                        self.porta_ = int(self.p.GetValue())
                        MyPanel.ip_classe = self.ip_
                        MyPanel.porta_classe = self.porta_
                        MyPanel.ip_unicast = self.c_
                        self.s = Socket_RL(self)
                        self.s.deamon=True
                        self.s.start()
                        self.countD.Enable(True)
                        self.btn.Enable(True)
                        self.Press.Disable()
                        self.rbox.Enable(False)
                        self.Press_u.Enable(True)
                        self.textarea_s.Clear()
                        self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))  
                            
            elif MyPanel.CHOOSE_T_METHOD == "Unicast":
                if addrinfo[0] == socket.AF_INET:
                    if str(self.c.GetValue().lower()) == "<broadcast>":
                         self.Warn("Warning! This IP is not a valid Unicast address!!!")
                    elif ipaddr.IPv4Address(str(self.i.GetValue().lower())).is_multicast == True \
                                          or ipaddr.IPv4Address(str(self.c.GetValue().lower())).is_multicast == True \
                                          or ipaddr.IPv4Address(str(self.i.GetValue().lower())).is_reserved == True \
                                          or ipaddr.IPv4Address(str(self.c.GetValue().lower())).is_reserved == True \
                                          or ipaddr.IPv4Address(str(self.i.GetValue().lower())).is_loopback == True \
                                          or ipaddr.IPv4Address(str(self.c.GetValue().lower())).is_loopback == True \
                                          or self.i.GetValue().lower() != \
                                              netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr']:
                        self.Warn("Warning! This IP is not a valid Unicast address!!!")
                    elif str(self.i.GetValue().lower()) == str(self.c.GetValue().lower()):
                        self.Warn("Warning! In Unicast transmission Detination and Source Address can not be the same!!!")
                    else:
                        self.ip_ = str(self.i.GetValue().lower())
                        self.c_ = str(self.c.GetValue().lower()) 
                        self.porta_ = int(self.p.GetValue())
                        MyPanel.ip_classe = self.ip_
                        MyPanel.porta_classe = self.porta_
                        MyPanel.ip_unicast = self.c_
                        self.s = Socket_RL(self)
                        self.s.deamon=True
                        self.s.start()
                        self.countD.Enable(True)
                        self.btn.Enable(True)
                        self.Press.Disable()
                        self.rbox.Enable(False)
                        self.Press_u.Enable(True)
                        self.textarea_s.Clear()
                        self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))
                else:
                     if str(self.c.GetValue().lower()) == "<broadcast>":
                         self.Warn("Warning! This IPv6 is not a valid Unicast address!!!")
                     elif ipaddr.IPv6Address(str(self.i.GetValue().lower())).is_multicast == True \
                                          or ipaddr.IPv6Address(str(self.c.GetValue().lower())).is_multicast == True \
                                          or ipaddr.IPv6Address(str(self.i.GetValue().lower())).is_reserved == True \
                                          or ipaddr.IPv6Address(str(self.c.GetValue().lower())).is_reserved == True \
                                          or ipaddr.IPv6Address(str(self.i.GetValue().lower())).is_loopback == True \
                                          or ipaddr.IPv6Address(str(self.c.GetValue().lower())).is_loopback == True \
                                          or self.i.GetValue().lower() != \
                                          netifaces.ifaddresses(netifaces.gateways()[2][0][1])[10][0]['addr']:
                                              self.Warn("Warning! This IPv6 is not a valid Unicast address!!!")
                     elif str(self.i.GetValue().lower()) == str(self.c.GetValue().lower()):
                        self.Warn("Warning! In Unicast transmission Detination and Source Address can not be the same!!!")
                     else:
                        self.ip_ = str(self.i.GetValue().lower())
                        self.c_ = str(self.c.GetValue().lower()) 
                        self.porta_ = int(self.p.GetValue())
                        MyPanel.ip_classe = self.ip_
                        MyPanel.porta_classe = self.porta_
                        MyPanel.ip_unicast = self.c_
                        self.s = Socket_RL(self)
                        self.s.deamon=True
                        self.s.start()
                        self.countD.Enable(True)
                        self.btn.Enable(True)
                        self.Press.Disable()
                        self.rbox.Enable(False)
                        self.Press_u.Enable(True)
                        self.textarea_s.Clear()
                        self.textarea_s.SetDefaultStyle(wx.TextAttr(wx.BLUE))

        except socket.error:
            self.Warn("Please, check the fields IP and port, network interface disabled or other error!!!")

    #-------------------------------------------------------------------
    # Close Socket_RL()
    def close_socket(self, event):
        self.OnExitApp(event)

    
    #-------------------------------------------------------------------
    #Run client to manual send message
    def run_client(self,event):
        """Client level One"""
        IP_=self.ip_ #Server, me
        try:
            addrinfo = socket.getaddrinfo(self.ip_, None)[0]
            #Create a SOcket UDP and assign local IP
            self.client = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
            #Time-to-live
            ttl = struct.pack('@i', 8) # LANs ttl < 32, and MAN, WAN, etc, ttl > 32.
            if addrinfo[0] == socket.AF_INET: # IPv4
                if self.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    #Send a message by multicast
                    self.client.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
                elif self.CHOOSE_T_METHOD == "Broadcast": #BROADCAST
                    #Send a message by broadcast
                    self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    IP_ = self.c_.lower() 
                else: #UNICAST
                    IP_= self.c_ 
            else: # IPv6 
                if self.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    self.client.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl)
                else: #UNICAST
                    IP_= self.c_ 
                    
            #Take local date/time and send to others processes
            data_a = datetime.now()
            #format date/time
            self.texto = data_a.strftime("%m/%d/%Y %H:%M:%S.%f")
            #coding date/time
            message = self.texto.encode('ascii')+b" Normal"
            #Count and log transmission event -> Step one Lamport Algorithm
            varglobal.soma += 1
            #Step two Lamport Algorithm
            message += b" "+str(varglobal.soma).encode('ascii')
            #sending date/time to others process
            self.client.sendto(message,(IP_, self.porta_))
            if MyPanel.CHOOSE_T_METHOD == "Unicast" or self.ip_ == netifaces.ifaddresses(netifaces.gateways()[2][0][1])[2][0]['addr']:
                self.client.sendto(message,(self.ip_, self.porta_))
            #catch local socket
            MyPanel.S_local = self.client.getsockname()
        except socket.error as msg:
            self.textDisplay.write("SOCKET ERROR (C)!!!, "+str(msg)+"\n")
            #sys.exit()


    #-------------------------------------------------------------------
    #Warns remote processes that this application will close
    def close_warning(self,event):
        """Client Level: warns before frame close"""
        IP_w=self.ip_
        try:
            addrinfo = socket.getaddrinfo(self.ip_, None)[0]
            #Create a SOcket UDP and assign local IP
            self.close = socket.socket(addrinfo[0], socket.SOCK_DGRAM)
            #Time-to-live
            ttl = struct.pack('@i', 8) # LANs ttl < 32, and MAN, WAN, etc, ttl > 32.
            if addrinfo[0] == socket.AF_INET: # IPv4
                if MyPanel.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    #Send a message by multicast
                    self.close.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
                elif MyPanel.CHOOSE_T_METHOD == "Broadcast": #BROADCAST
                    #Send a message by broadcast
                    self.close.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    IP_w = self.c_.lower()
                else: #UNICAST
                    IP_w= self.c_ 
            else: # IPv6 
                if MyPanel.CHOOSE_T_METHOD == "Multicast": #MULTICAST
                    self.close.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl)
                else: #UNICAST
                    IP_w= self.c_ 
            
            #Take local date/time and send to others processes
            data_close = datetime.now()
            #format date/time
            close_msg = data_close.strftime("%m/%d/%Y %H:%M:%S.%f")
            msg_c = close_msg.encode('ascii')+b" CLOSE" 
            
            #Count and log transmission event -> Step one Lamport Algorithm
            varglobal.soma += 1
            #Step two Lamport Algorithm
            msg_c += b" "+str(varglobal.soma).encode("ascii")
            #sending date/time to others process
            self.close.sendto(msg_c, (IP_w, self.porta_))
        except socket.error as msg:
            self.textDisplay.write("SOCKET ERROR (CLOSE), "+str(msg)+"\n")
            #sys.exit()

    #-------------------------------------------------------------------
    #Destroys the main frame when exit of the wxPython app
    def OnExitApp(self, event):
        try:
            self.close_warning(event)
            self.Destroy()
        except:
            self.Destroy()
            
           
if __name__ == "__main__":
    app = wx.App()
    frame = MyPanel(parent=None, id=-1)
    frame.Show()
    frame.countD.Enable(False)
    frame.btn.Enable(False)
    frame.Press_u.Enable(False)
    frame.stop.Enable(False)
    frame.Info("WARNING!!! Before send a message/synchronize, please verify Transmission Method, \
communication ports, and IP Version!")
    app.MainLoop()
