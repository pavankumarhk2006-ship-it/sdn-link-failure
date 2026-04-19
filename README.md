# SDN Link Failure Detection and Recovery

## Objective
To detect link failures and dynamically reroute traffic using a Ryu SDN controller.

## Concept
- Uses Ryu controller with OpenFlow
- Detects link failure using PortStatus events
- Clears flow entries on failure
- Re-learns paths and reroutes traffic

## Topology
h1 --- s1 ---- s2 ---- s3 --- h2
 \___________ s3 ___________/

## How to Run

1. Start controller:
   ryu-manager controller.py

2. Start Mininet:
   sudo mn --custom topo.py --topo mytopo --controller remote

3. Test:
   h1 ping h2
   link s1 s2 down

## Output
- Ping works normally
- After link failure → small packet loss
- Then ping continues (rerouted)

## Result
Traffic continues even after link failure using alternate path.

## Conclusion
The system dynamically adapts to link failures and maintains connectivity using SDN.

Author:Pavan Kumar H K
SRN:PES1UG24CS319
SUBJECT:COMPUTER NETWORKS
