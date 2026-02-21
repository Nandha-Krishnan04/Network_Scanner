import socket
from mac_vendor_lookup import MacLookup
from scapy.all import IP, ICMP, sr1

mac_lookup = MacLookup()

def get_myip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def host_name(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "No hostname"

def get_vendor(mac):
    try:
        return mac_lookup.lookup(mac)
    except:
        return "Unknown"

def ttl_find(ttl):
    if ttl is None:
        return "No response"
    if ttl >= 250:
        return "Router / Network Device"
    elif 100 <= ttl <= 130:
        return "Windows"
    elif 60 <= ttl < 100:
        return "Linux / macOS / Android"
    else:
        return "Unknown"

def guess_device(ip):
    try:
        packet = IP(dst=ip)/ICMP()
        reply = sr1(packet, timeout=2, verbose=False)
        if reply:
            return ttl_find(reply.ttl)
        else:
            return "No ICMP response"
    except:
        return "Error detecting"