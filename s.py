from scapy.all import *
packet = IP()/TCP()
e_pack = Ether()/packet
e_pack.show()


from scapy.all import *
packets = sniff(count=10)
packets.summary()
print(packets[0].show())
print(packets[1].show())


from scapy.all import *
result, unanswered = traceroute(["www.example.com", "www.google.com"], maxttl=20)
result.show()


import scapy.all as scapy
request = scapy.ARP()
request.pdst = "192.168.1.1/28"
broadcast = scapy.Ether()
broadcast.dst = "ff:ff:ff:ff:ff:ff"
request_broadcast = broadcast / request
clients = scapy.srp(request_broadcast, timeout=2)[0]
for element in clients:
    print(element[1].psrc + " - " + element[1].hwsrc)


from scapy.all import *
packet = IP(dst="8.8.8.8")/ICMP()
send(packet)


from scapy.all import *
target = "www.example.com"
for port in range(20, 25):
    packet = IP(dst=target) / TCP(dport=port, flags="S")
    response = sr1(packet, timeout=1, verbose=0)
    if response:
        print("Port", port, "is open")


from scapy.all import *
def callback(packet):
    if packet.haslayer(ICMP):
        print("ICMP Packet Detected")
        packet.show()

sniff(filter="icmp", prn=callback, count=10)
