def generate_protocol_mapping():
    # Protocol number to protocol name mapping
    protocol_number_mapping = {
        0: "HOPOPT", 1: "ICMP", 2: "IGMP", 3: "GGP", 4: "IP-in-IP", 5: "ST", 6: "TCP", 7: "CBT",
        8: "EGP", 9: "IGP", 10: "BBN-RCC-MON", 11: "NVP-II", 12: "PUP", 13: "ARGUS", 14: "EMCON",
        15: "XNET", 16: "CHAOS", 17: "UDP", 18: "MUX", 19: "DCN-MEAS", 20: "HMP", 21: "PRM",
        22: "XNS-IDP", 23: "TRUNK-1", 24: "TRUNK-2", 25: "LEAF-1", 26: "LEAF-2", 27: "RDP",
        28: "IRTP", 29: "ISO-TP4", 30: "NETBLT", 31: "MFE-NSP", 32: "MERIT-INP", 33: "DCCP",
        34: "3PC", 35: "IDPR", 36: "XTP", 37: "DDP", 38: "IDPR-CMTP", 39: "TP++", 40: "IL",
        41: "IPv6", 42: "SDRP", 43: "IPv6-Route", 44: "IPv6-Frag", 45: "IDRP", 46: "RSVP",
        47: "GRE", 48: "DSR", 49: "BNA", 50: "ESP", 51: "AH", 52: "I-NLSP", 53: "SWIPE",
        54: "NARP", 55: "MOBILE", 56: "TLSP", 57: "SKIP", 58: "IPv6-ICMP", 59: "IPv6-NoNxt",
        60: "IPv6-Opts", 61: "Any host internal protocol", 62: "CFTP", 63: "Any local network",
        64: "SAT-EXPAK", 65: "KRYPTOLAN", 66: "RVD", 67: "IPPC", 68: "Any distributed file system",
        69: "SAT-MON", 70: "VISA", 71: "IPCU", 72: "CPNX", 73: "CPHB", 74: "WSN", 75: "PVP",
        76: "BR-SAT-MON", 77: "SUN-ND", 78: "WB-MON", 79: "WB-EXPAK", 80: "ISO-IP", 81: "VMTP",
        82: "SECURE-VMTP", 83: "VINES", 84: "TTP", 85: "NSFNET-IGP", 86: "DGP", 87: "TCF",
        88: "EIGRP", 89: "OSPFIGP", 90: "Sprite-RPC", 91: "LARP", 92: "MTP", 93: "AX.25",
        94: "IPIP", 95: "MICP", 96: "SCC-SP", 97: "ETHERIP", 98: "ENCAP", 99: "GMTP", 
        100: "IFMP", 101: "PNNI", 102: "PIM", 103: "ARIS", 104: "SCPS", 105: "QNX", 
        106: "A/N", 107: "IPComp", 108: "SNP", 109: "Compaq-Peer", 110: "IPX-in-IP", 
        111: "VRRP", 112: "PGM", 113: "any 0-hop protocol", 114: "L2TP", 115: "DDX", 
        116: "IATP", 117: "STP", 118: "SRP", 119: "UTI", 120: "SMP", 121: "SM", 122: "PTP", 
        123: "ISIS", 124: "FIRE", 125: "CRTP", 126: "CRUDP", 127: "SSCOPMCE", 128: "IPLT", 
        129: "SPS", 130: "PIPE", 131: "SCTP", 132: "FC", 133: "RSVP-E2E-IGNORE", 134: "Mobility Header", 
        135: "UDPLite", 136: "MPLS-in-IP", 137: "manet", 138: "HIP", 139: "Shim6", 140: "WESP", 
        141: "ROHC", 142: "Ethernet"
    }

    # Save the protocol number to protocol name mapping to a .txt file
    protocol_mapping_entries = [f"{protocol},{name}" for protocol, name in protocol_number_mapping.items()]

    with open("protocol_number_mapping.txt", "w") as file:
        file.write("\n".join(protocol_mapping_entries))

    print("Protocol mapping generated and saved to protocol_number_mapping.txt")

