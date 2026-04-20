# SDN Traffic Monitoring using POX and Mininet

## Overview

This project demonstrates Software Defined Networking (SDN) traffic monitoring using the POX controller and Mininet emulator.

The controller dynamically installs flow rules and monitors network traffic in real time.

## Technologies Used

* POX Controller
* Mininet Network Emulator
* Open vSwitch
* Python

## Network Topology

Single switch topology with 3 hosts.

```
h1 -----\
         \
          s1 ----- Controller
         /
h2 -----/

h3 -----/
```

## Installation

### Install Mininet

```
sudo apt update
sudo apt install mininet
```

### Clone POX

```
git clone https://github.com/noxrepo/pox.git
cd pox
```

## Running the Controller

```
cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning ext.traffic_monitor
```

## Running the Network

Open a new terminal and run:

```
sudo mn --topo single,3 --mac --switch ovsk --controller remote
```

## Testing Connectivity

Inside Mininet:

```
pingall
```

## Performance Testing

```
iperf
```

## Flow Table Inspection

```
dpctl dump-flows
```

## Results

The controller successfully monitors traffic and installs flow rules dynamically in the OpenFlow switch.

## Screenshots

Screenshots of controller logs, topology, and traffic monitoring are included in the screenshots folder.

## Conclusion

This project demonstrates a basic SDN architecture where a centralized controller manages network traffic and flow rules dynamically.
