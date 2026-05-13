# LLCTT — Lamport Logical Clock Teaching Tool

![LLCTT Linux](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/gui1.png)

**Lamport Logical Clock Teaching Tool (LLCTT)** is an educational software tool for teaching and experimenting with concepts from **Distributed Systems**, especially **Lamport Logical Clocks**, distributed event ordering, message exchange, and clock synchronization.

The tool allows students and instructors to visualize logical clocks, physical clock updates, communication between processes, and distributed synchronization using IPv4 and IPv6 networks.

LLCTT is distributed for **Linux** and **Windows**. In both versions, the user does **not** need to manually install Python, wxPython, or external libraries. The required runtime components are already packaged with the application.

---

## Main Features

- Didactic graphical interface for Distributed Systems classes.
- Lamport Logical Clock visualization.
- Logical and physical clock synchronization.
- IPv4 and IPv6 support.
- UDP communication.
- Unicast, Broadcast, and Multicast transmission modes.
- Local and remote process monitoring.
- Distributed event panel.
- Logical clock counter panel.
- Physical clock panel.
- Time difference panel.
- RTT-based adjustment inspired by Cristian's algorithm.
- Manual and automatic message sending.
- Linux containerized version.
- Windows packaged executable version by Nuitka.
- 7-day trial mode.
- Machine-bound license validation.
- Anti-rollback and anti-tampering protection.

---

## Educational Purpose

LLCTT was designed to support practical teaching of Distributed Systems topics, including:

- Lamport Logical Clocks;
- ordering of distributed events;
- logical time versus physical time;
- message passing between processes;
- synchronization through network communication;
- Unicast, Broadcast, and Multicast behavior;
- IPv4 and IPv6 socket communication.

The tool helps students observe how distributed processes exchange messages, update logical clocks, and synchronize events in real time.

---

## Basic Concept

In Distributed Systems, physical clocks are not always reliable for ordering events. Lamport Logical Clocks provide a logical mechanism for defining the causal order of events.

If an event `a` happens before an event `b`, then the logical timestamp of `a` must be smaller than the logical timestamp of `b`:

```text
if a → b, then C(a) < C(b)
```

The basic Lamport rule used by LLCTT is:

```text
1. Before a local event, increment the local logical clock.
2. When sending a message, attach the current logical timestamp.
3. When receiving a message, update the local logical clock using:

   Cj = max(Cj, ts(m)) + 1
```
## Pseudo Code Lamport Logical Clock Algorithm
![Pseudo Code](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/algo.png)

---

# LLCTT Software Registration

### The LLCTT has been officially registered with the Instituto Nacional da Propriedade Industrial (INPI), ensuring the legal protection of its intellectual property in Brazil. This registration reinforces the originality and technological relevance of the tool, which was developed to support the teaching and practical understanding of distributed systems concepts, especially Lamport logical clocks and network communication mechanisms.

![INPI Registration](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/certificado.png)

## Example of Operation
![Operation](https://github.com/dioxfile/Vector_Clock/raw/master/Imagens/3.png)

### Illustration of the LLCTT broadcast synchronization process using Lamport logical clocks. The figure demonstrates how a node propagates a broadcast time reference (Bcst T) to other distributed nodes, allowing clients to update their local logical time (UTB) according to the received synchronization message and returned broadcast time (TRB).
---

## Supported Platforms

| Platform | Distribution Model | Manual Dependencies Required |
|---|---|---|
| Linux | Docker container | No |
| Windows 10/11 | Packaged executable | No |

---

# Linux Version 🐧

The Linux version is distributed as a **containerized application** with graphical interface support through X11 🐧.

The user does not need to install Python, wxPython, netifaces, dateutil, PyPubSub, or any other Python dependency manually.

## Linux Requirement

Only the following is required:

```text
Docker must be installed and working, but if the user does not have it, a Docker 🐳 installation script is provided with LLCTT (e.g., install_docker.sh).
```

Docker Compose 📦 must also be available. In most recent Docker installations, Compose is already included.

---

## Linux Delivered Files

The Linux package may include:

```text
activate_license.sh
docker-compose.yml
get_machine-id.sh
install_docker.sh
install.sh
llctt.tar
README_CLIENT.txt
repair_client.sh
run.sh
stop.sh
```

---

## Linux Installation

Open a terminal in the LLCTT folder and run:

```bash
chmod +x install.sh run.sh stop.sh activate_license.sh
./install.sh
```

This loads the LLCTT Docker image and prepares the application environment.

---

## Linux Execution

To start LLCTT:

```bash
./run.sh
```

To stop LLCTT:

```bash
./stop.sh
```

If the application needs to modify the system clock, it must run with the required system permissions configured in the container package.

---

## Linux Machine-ID

The license is bound to the machine. To obtain the Linux machine identifier, run:

```bash
cat /etc/machine-id
```

Send the generated value to the software provider to request a license.

---

## Linux License Activation

After receiving the license file named:

```text
license.json
```

activate it with:

```bash
./activate_license.sh license.json
```

Then restart LLCTT:

```bash
./stop.sh
./run.sh
```

---

# Windows Version 🪟

The Windows version is distributed as a packaged executable.

The user does not need to install Python, Visual Studio Build Tools, wxPython, pip packages, or any other dependency manually.

---
## Windows Delivered Files

The Windows package may include:

```text
LLCTT_Setup_v1.0.exe
activate_license.bat
get_machine-id.bat
machine_fingerprint.py
README_WINDOWS.txt
```
### OBS: Python is only a prerequisite for running the machine_fingerprint.py file.

## Windows Installation

1. Extract the LLCTT Windows package.
2. Keep all files in the same folder.
3. Do not rename or modify internal files.
4. Run the executable as Administrator.

Install Example:

```text
LLCTT_Setup_v1.0.exe
```
### After that, run LLCTT.exe (Desktop Ico).
Administrator permission is recommended because LLCTT may need to access network resources and adjust the system clock.

---

## Windows Execution

Right-click the executable (e.g., LLCTT.exe (Desktop Ico)) and select:

```text
Run as administrator
```

If Windows Defender or another security tool asks for confirmation, allow execution only if the package was received from the official software provider.

---

## Windows Firewall Notes

For network communication tests, Windows Firewall may need to allow ICMP and local network communication.

Open PowerShell as Administrator and run:

```powershell
firewall.cpl
```

Then enable, when necessary:

```text
File and Printer Sharing (Echo Request - ICMPv4-In);
File and Printer Sharing (Echo Request - ICMPv6-In);
Virtual Machine Monitoring (Echo Request - ICMPv4-In);
Virtual Machine Monitoring (Echo Request - ICMPv6-In).
```

In laboratory environments, also verify whether UDP communication is allowed on the selected LLCTT port.

---

## Windows Machine-ID

Open PowerShell as Administrator and run one of the following commands:

```powershell
wmic csproduct get uuid
```

or:

```powershell
Get-ComputerInfo | Select-Object CsSystemUUID
```
or run:
```PowerShell
.\get_machine-id.bat
```
Send the generated identifier to the software provider to request a license. Link: [LLCTT Owner](https://www.linkedin.com/in/dioxfile).

---

## Windows License Activation

Place the received file:

```text
license.json
```

inside the LLCTT application folder.

Then run LLCTT again as Administrator.

If the Windows package includes a specific activation script, use it according to the client instructions provided with the package.

---

# Trial Mode

When no valid license is found, LLCTT may start in **trial mode**.

Current trial period:

```text
7 days
```

After the trial expires, a valid license is required.

---

# Licensing System

LLCTT uses a local licensing system with:

- machine identification;
- signed license file;
- expiration date validation;
- trial period control;
- anti-rollback verification;
- anti-tampering checks.

A license is valid only for the machine for which it was issued.

---

# Anti-Rollback Protection

LLCTT includes protection against system clock rollback and runtime state manipulation.

The system may block execution when it detects:

- manual system clock rollback;
- VM snapshot rollback;
- license state tampering;
- trial state manipulation;
- inconsistent runtime state.

If a message such as the following appears:

```text
System clock rollback detected
```

or:

```text
Runtime state has been tampered with
```

contact the software provider. Do not manually edit internal files.

---

# How to Use LLCTT

## 1. Start the Application

Linux:

```bash
./run.sh
```

Windows:

```text
Run LLCTT.exe as Administrator
```

---

## 2. Choose the Communication Mode

LLCTT supports:

```text
Unicast
Broadcast
Multicast
```

The correct option depends on the teaching activity and the local network environment.

---

## 3. Configure IP and Port

Typical examples:

```text
IPv4 local server: 0.0.0.0
Broadcast address: <broadcast>
Port: 10001
```

Any available UDP port may be used, provided it is not already in use by another application.

---

## 4. Bind the Socket

After selecting the IP address, port, and transmission mode, click the bind/connect button in the graphical interface.

The local socket information will be displayed in the application.

---

## 5. Send Messages

LLCTT supports:

```text
Manual Send Message
Automatic Send Message
Stop Automatic Message
```

Each message generates distributed events and updates the logical clock panel.

---

## 6. Observe the Panels

The main panels show:

- local events;
- remote events;
- local logical clock;
- physical clock;
- known hosts/processes;
- time difference;
- RTT delay;
- synchronization updates.

---

# Network Notes

For best results:

- use machines connected to the same local network;
- allow UDP traffic on the selected port;
- enable ICMP echo when RTT measurement is required;
- test Broadcast and Multicast according to the network policy;
- verify IPv6 scope when using IPv6 Multicast.

On Windows, some IPv6 Multicast scenarios may require a more specific scope, depending on the network interface and operating system configuration.

---

# Important Recommendations

- Run LLCTT as Administrator/root when clock adjustment is required.
- Do not modify internal files.
- Do not edit `license.json` manually.
- Do not delete runtime state files.
- Avoid system clock rollback.
- Avoid restoring old VM snapshots after trial or license activation.
- Keep the original package structure.

---

# Screenshots

## Linux

![LLCTT Linux](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/LogicClock.png)

## Windows

![LLCTT Windows](https://github.com/dioxfile/Vector_Clock/blob/master/Imagens/gui-win.png)

---

# Academic and Institutional Use

LLCTT is suitable for:

- Distributed Systems courses;
- Computer Networks laboratories;
- operating systems classes;
- practical demonstrations of logical clocks;
- academic experiments involving distributed event ordering.

---

# Usage Rights

This software is licensed for authorized use only.

Unauthorized reproduction, redistribution, reverse engineering, tampering, or license circumvention is prohibited.

---

# Support

For licensing, activation, or technical support, contact the software provider.

**Developer / Provider:** Diógenes Antônio Marques José
**Institution:** Universidade do Estado de Mato Grosso — UNEMAT

---

# LLCTT – Lamport Logic Clock Teaching Tool - Platform Notes

## Linux

LLCTT runs inside a preconfigured containerized environment on Linux.

All required dependencies are already included in the container image.

---

## Windows

On Windows, LLCTT does not require manual installation of Python or additional APIs for end users.

All dependencies are already bundled inside the LLCTT executable package generated with Nuitka's standalone mode.

Windows users only need to:

- Install the LLCTT executable package
- Run LLCTT as Administrator

---

# Administrator Privileges

LLCTT must be executed with administrator/root privileges because the application:

- Uses multicast sockets
- Performs low-level networking operations
- Accesses privileged socket APIs
- Modifies or synchronizes the operating system date and time

---

# IPv6 Multicast Notes

Linux generally provides stable IPv6 multicast support.

Windows is significantly more restrictive regarding IPv6 multicast, especially inside virtualized environments such as:

- VirtualBox
- VMware

During testing, the most reliable multicast scope on Windows virtual machines was:

```text
ff03::/16
```

particularly:

```text
ff03::1
```

Although functional, IPv6 multicast on Windows may still present instability depending on:

- hypervisor
- VM network mode
- firewall configuration
- network adapter driver
- multicast scope handling

---

# Recommended Configuration

## Linux

Recommended for IPv6 multicast experiments.

## Windows

Prefer:

- IPv4 Unicast
- IPv4 Broadcast
- IPv4 Multicast

---

# Virtual Machines

For VirtualBox and VMware:

- Use Bridged Networking / Bridged Adapter
- Avoid NAT mode during multicast experiments

---

# Firewall Considerations

If communication problems occur:

- Allow LLCTT through the firewall
- Allow UDP traffic on the selected port
- Temporarily disable the firewall for testing purposes

---

# Final Recommendation

For best operational stability:

- Use Linux whenever possible for IPv6 multicast experiments
- Execute LLCTT with administrator/root privileges
- Prefer Bridged networking in virtualized environments

---

For further clarification, please read the LLCTT Operational Considerations PDF.

# Reference

Lamport, L. (1978). *Time, Clocks, and the Ordering of Events in a Distributed System*. Communications of the ACM.
