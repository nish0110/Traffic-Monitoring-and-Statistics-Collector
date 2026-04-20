
# SDN Traffic Monitoring using POX and Mininet

Software Defined Networking project demonstrating real-time traffic monitoring using the POX controller and Mininet emulator.

---

## Overview

This project demonstrates Software Defined Networking (SDN) traffic monitoring using the POX controller and Mininet emulator.

The controller dynamically installs flow rules and monitors network traffic in real time.

---

## Technologies Used

* POX Controller
* Mininet Network Emulator
* Open vSwitch
* Python

---

## Network Topology

Single switch topology with 3 hosts.

```

h1 -----

s1 ----- Controller
/
h2 -----/

h3 -----/

```

---

## Installation

### Install Mininet

```

sudo apt update
sudo apt install mininet

```

### Clone POX

```

git clone [https://github.com/noxrepo/pox.git](https://github.com/noxrepo/pox.git)
cd pox

```

---

## Running the Controller

```

cd ~/pox
./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning ext.traffic_monitor

```

---

## Running the Network

Open a new terminal and run:

```

sudo mn --topo single,3 --mac --switch ovsk --controller remote

```

---

## Testing Connectivity

Inside Mininet:

```

pingall

```

---

## Controlled Traffic Generation

Controlled traffic generation allows specific traffic to be generated between hosts so that the SDN controller can monitor packet statistics.

Example command:

```

h1 ping -c 20 h2

```

Explanation:

* Host **h1** sends 20 ICMP packets to **h2**
* The controller captures these packets
* Traffic statistics such as packet counts and byte counts are updated in the controller logs

This demonstrates real-time monitoring of network traffic.

---

## View Host Interfaces

To view network interface details of a host:

```

h1 ifconfig

```

Example output shows:

* IP Address
* MAC Address
* Interface status

Example:

```

h1-eth0: flags=4163
inet 10.0.0.1
ether 00:00:00:00:00:01

```

This confirms that the hosts are correctly configured in the Mininet network.

---

## Show Switch Information

To inspect the Open vSwitch configuration and controller connection:

```

sh ovs-vsctl show

```

This command displays:

* Switch ID
* Connected controller
* Available ports
* Bridge configuration

Example output:

```

Bridge s1
Controller "tcp:127.0.0.1:6633"
Port s1-eth1
Port s1-eth2
Port s1-eth3

```

This verifies that the switch is connected to the SDN controller.

---

## Host Routing Table

To display the routing table of a host:

```

h1 route -n

```

Example output:

```

Destination     Gateway     Genmask
10.0.0.0        0.0.0.0     255.0.0.0

```

This shows how packets are routed within the Mininet network.

---

## Performance Testing

```

iperf

```

---

## Flow Table Inspection

```

dpctl dump-flows

```

---

## Results

The controller successfully monitors traffic and installs flow rules dynamically in the OpenFlow switch.

---

## Screenshots

Screenshots of controller logs, topology, and traffic monitoring are included in the screenshots folder.

---
### Demo
[Click here to view the Video Demo](https://drive.google.com/drive/folders/1yaUqgmYh8xXA8drze81ETVtpfllhtV55)

## Future Improvements

Possible extensions of this project include:

* Real-time traffic visualization dashboard
* Integration with machine learning for anomaly detection
* Support for multiple switches and larger topologies
* Automated traffic report generation

---

## Author

Nishitha Padanthaya

---

