from scapy.all import ARP, Ether, srp
import hostdetails

def arp_scan(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    answered = srp(packet, timeout=2, verbose=False)[0]

    hosts = []

    for sent, received in answered:
        vendor = hostdetails.get_vendor(received.hwsrc)
        hostname = hostdetails.host_name(received.psrc)
        device = hostdetails.guess_device(received.psrc)

        hosts.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "vendor": vendor,
            "device": device,
            "hostname": hostname
        })

    return hosts