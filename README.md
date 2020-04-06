# VCIOUS_DNS
![](roses.gif)

VCIOUS_DNS is a DNS spoofing tool, simple yet affective...
modifies dns response.

# project

  - VCIOUS_DNS.py
  - iptables.sh
  - ipflush.sh
  - var.py

# Requirements

  - Python3
  - scapy
  - netfilterqueue
  - VCIOUS_ARP.py (github.com/vciousvctorious/VCIOUS_ARP)
 
# usage:

  - SU
  - Modify var.py to specify your target url, ip
  - Run VCIOUS_ARP.py (READ github.com/vciousvctorious/VCIOUS_ARP)
  - python3 VCIOUS_DNS.py
  - Note: closing the script without ctrl+c might cause networking issues
  - Fix the issue above by running : sh ipflush.sh

# NOTES

  - If you are trying to spoof https, keep in mind that browsers\ 
got a protocol log, so PLEASE configure https in your server

## Twitter : https://twitter.com/vciousvctorious
## GitHub  : https://github.com/vciousvctorious
