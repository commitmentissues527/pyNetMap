# pyNetMap

pyNetMap
pyNetMap is a lightweight Python tool that scans your local private subnet, detects live devices, and visualizes your network topology in a clean, router-centric graph.

Sample Output:
Router (192.168.1.1)
├── 192.168.1.10 (Host A)
├── 192.168.1.15 (Host B)
└── 192.168.1.42 (Host C)

Features:

ARP-based local subnet scanning

IP, MAC, and optional hostname detection

Central router as the root node of the graph

Visual output using networkx and matplotlib

Works offline on private networks

Requirements:

Python 3.10 or 3.11

Windows OS

Npcap (required for Scapy to work)

To install required dependencies:
pip install scapy networkx matplotlib

Usage:
Run as administrator to allow low-level packet sending:
python pyNetMap.py

How it Works:

Detects the local default gateway (e.g., 192.168.1.1)

Scans the subnet (e.g., 192.168.1.0/24) using ARP requests

Collects live IP addresses and MAC addresses

Optionally performs reverse DNS lookups to identify hostnames

Constructs a graph where the router is the central node and each connected device branches off

Displays IP above each node, MAC address and optionally hostname below

Limitations:

Hostname resolution may be slow or unavailable depending on the network

Only shows devices on the same subnet as the host machine

This tool is intended for educational and private use only


