# SDN Link Failure Detection and Recovery using Ryu & Mininet

## 👤 Student Details

**Name:** Pavan Kumar H K
**SRN:** PES1UG24CS319

---

## 📌 Project Objective

This project demonstrates how Software Defined Networking (SDN) can dynamically handle network changes such as link failures. Using a Ryu controller and Mininet, the system detects link failures, updates flow rules, and restores connectivity automatically.

---

## 🛠️ Tools & Technologies

* Mininet (Network Emulator)
* Ryu Controller (SDN Controller)
* OpenFlow 1.3 Protocol
* Python

---

## 🌐 Network Topology

A linear topology with 3 switches and 3 hosts:

```
h1 ─ s1 ─ s2 ─ s3 ─ h3
        │
        h2
```

* h1 connected to s1
* h2 connected to s2
* h3 connected to s3

---

## ⚙️ Features Implemented

* Learning Switch using Ryu
* Flow rule installation (match-action)
* Link failure detection
* Dynamic flow update
* Network recovery after link restoration
* Flow table inspection using ovs-ofctl

---

## ▶️ Execution Steps

### 1. Clean Environment

```
sudo mn -c
pkill -f ryu-manager
```

### 2. Start Controller

```
cd ~/sdn-link-failure-final
source ~/ryu38-env/bin/activate
ryu-manager link_failure_fixed.py
```

### 3. Start Mininet

```
sudo mn --topo linear,3 --controller=remote
```

---

## 🧪 Testing & Demonstration

### ✅ Normal Operation

```
pingall
```

**Result:** 0% packet loss

---

### 🔍 Flow Table Check

```
sh ovs-ofctl dump-flows s2
```

Shows match-action flow rules installed by controller.

---

### 🔴 Link Failure Simulation

```
link s2 s3 down
pingall
```

**Result:** Partial packet loss (~66%)

* h1 ↔ h2 works
* h3 becomes unreachable

---

### 🟢 Link Restoration

```
link s2 s3 up
pingall
```

**Result:** 0% packet loss (network restored)

---

## 📊 Observations

* Flow rules are dynamically installed by the controller.
* During link failure, existing flows may remain but become invalid.
* After restoration, new flows are installed or reused.
* Packet counters in flow tables confirm active forwarding.

---

## 🧠 Key Concepts

* SDN separates control plane and data plane
* Controller manages network behavior centrally
* Flow rules follow match-action paradigm
* Table-miss rule sends unknown packets to controller

---

## 🎯 Conclusion

This project successfully demonstrates how SDN enables dynamic network management. The controller detects link failures, adapts flow rules, and restores connectivity efficiently, showcasing the flexibility and power of SDN.

---

## 📷 (Optional)

Add screenshots of:

* Flow tables
* Ping results
* Link failure logs

---

## 📎 References

* Ryu Documentation
* Mininet Documentation
* OpenFlow Specification
sudo mn -c
pkill -f ryu-manager
cd ~/sdn-link-failure-final
source ~/ryu38-env/bin/activate
ryu-manager link_failure_fixed.py
sudo mn --topo linear,3 --controller=remote
pingall
sh ovs-ofctl dump-flows s1
sh ovs-ofctl dump-flows s2
sh ovs-ofctl dump-flows s3
h1 ping h2
h1 ping h3
link s2 s3 down
pingall
h1 ping h2
h1 ping h3
sh ovs-ofctl dump-flows s2
link s2 s3 up
pingall
sh ovs-ofctl dump-flows s2
exit
