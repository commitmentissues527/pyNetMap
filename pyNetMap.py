from scapy.all import ARP, Ether, srp
import networkx as nx
import matplotlib.pyplot as plt
import os
import socket


def get_default_gateway():
        output = os.popen("ipconfig").read()
        for line in output.splitlines():
            if "Default Gateway" in line and ":" in line:
                ip = line.split(":")[-1].strip()
                if ip:
                    return ip
 
router_ip = get_default_gateway() 


target_ip = router_ip.rsplit('.', 1)[0] + '.0/24'
arp = ARP(pdst=target_ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether / arp
result = srp(packet, timeout=2, verbose=0)[0]


clients = []
for sent, received in result:
    ip = received.psrc
    mac = received.hwsrc

    
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "unknown"

    clients.append({'ip': ip, 'mac': mac, 'hostname': hostname})


G = nx.Graph()
G.add_node(router_ip, label="Router")

for client in clients:
    if client['ip'] != router_ip:  # Don't link the router to itself
        G.add_node(client['ip'], label=client['mac'])
        G.add_edge(router_ip, client['ip'])


plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G)


nx.draw(G, pos, node_size=1000, node_color='skyblue')


for node, (x, y) in pos.items():
    plt.text(x, y + 0.03, node, fontsize=12, ha='center', va='center', fontweight='bold')  # IP

# MAC + Hostname label below node
for node, (x, y) in pos.items():
    for client in clients:
        if client['ip'] == node:
            mac = client['mac']
            hostname = client['hostname']
            break
    label_text = f"{hostname}\n{mac}" if hostname != "unknown" else mac
    plt.text(x, y - 0.04, label_text, fontsize=10, ha='center', va='center', color='gray')


plt.suptitle("Private Network Topology (Router-Centric)", fontsize=16, y=1)  

plt.show()


