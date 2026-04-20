# SDN Link Failure Detection and Recovery

## 👤 Student Details
- Name: Pavan Kumar H K  
- SRN: PES1UG24CS319  

---

## 🎯 Objective
The objective of this project is to detect link failures in a network and automatically reroute traffic using Software Defined Networking (SDN), ensuring continuous communication without interruption.

---

## 🧠 Concept
In traditional networks, when a link fails, communication stops.  
In SDN, a central controller manages the network and can dynamically adapt to failures.

This project uses:
- **Ryu Controller** → Controls the network  
- **Mininet** → Simulates the network  
- **OpenFlow Protocol** → Communication between controller and switches  

The controller monitors the network, detects failures, updates flow rules, and reroutes traffic.

---

## 🏗️ Topology


h1 --- s1 ---- s2 ---- s3 --- h2
___________ s3 ___________/


- **Main Path:** s1 → s2 → s3  
- **Alternate Path:** s1 → s3  

The alternate path allows communication even if the main path fails.

---

## ⚙️ Working

1. When the network starts, the controller learns MAC addresses of hosts  
2. It installs flow rules in switches for efficient packet forwarding  
3. Packets are forwarded through the shortest path  

### 🔴 During Link Failure
- A link failure is simulated using:

link s1 s2 down

- The controller detects this using **PortStatus event**
- Old flow rules are cleared
- New flow rules are installed using the alternate path

### 🟢 After Recovery
- Packets are rerouted automatically  
- Communication continues with minimal packet loss  

---

## 🔍 Features
- Link failure detection  
- Dynamic flow rule update  
- Automatic rerouting  
- Continuous communication  
- Efficient packet forwarding  

---

## 🧪 How to Run

### 1. Start Controller
```bash
cd ~/sdn-link-failure-final
source ~/ryu/ryu-env/bin/activate
ryu-manager controller.py
2. Start Mininet
cd ~/sdn-link-failure-final
sudo mn --custom topo.py --topo mytopo --controller remote
3. Test Connectivity
h1 ping h2
4. Simulate Link Failure
link s1 s2 down
