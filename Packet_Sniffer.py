from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Packet counter and limit
packet_count = 0
packet_limit = 0

# Function to display colored output
def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

# Packet handler function to analyze captured packets
def packet_callback(packet):
    global packet_count
    
    packet_count += 1
    
    # Timestamp for the packet
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        protocol = ip_layer.proto

        # Display packet header
        print(f"{Fore.MAGENTA}[#] Packet {packet_count} @ {timestamp}{Style.RESET_ALL}")
        
        # Display source and destination IPs
        print_colored(f"Source IP: {src_ip}", Fore.CYAN)
        print_colored(f"Destination IP: {dst_ip}", Fore.CYAN)
        
        # Determine the protocol and display it
        if protocol == 6:  # TCP protocol
            print_colored("Protocol: TCP", Fore.GREEN)
            if TCP in packet:
                print_colored(f"Source Port: {packet[TCP].sport}", Fore.YELLOW)
                print_colored(f"Destination Port: {packet[TCP].dport}", Fore.YELLOW)
        elif protocol == 17:  # UDP protocol
            print_colored("Protocol: UDP", Fore.GREEN)
            if UDP in packet:
                print_colored(f"Source Port: {packet[UDP].sport}", Fore.YELLOW)
                print_colored(f"Destination Port: {packet[UDP].dport}", Fore.YELLOW)
        elif protocol == 1:  # ICMP protocol
            print_colored("Protocol: ICMP", Fore.GREEN)
        else:
            print_colored(f"Protocol: Other ({protocol})", Fore.RED)

        # Display payload (if any)
        if packet[IP].payload:
            payload = bytes(packet[IP].payload)
            print_colored(f"Payload: {payload[:32]}...", Fore.MAGENTA)  # Showing first 32 bytes of payload
            
        # Divider
        print(Fore.BLUE + "-" * 50 + Style.RESET_ALL)

# Stop sniffing after reaching packet limit
def stop_sniff(packet):
    return packet_count >= packet_limit

# Start sniffing (Ctrl+C to stop)
if __name__ == "__main__":
    print(Fore.YELLOW + "Starting cool packet sniffer...\n" + Style.RESET_ALL)

    # Ask the user how many packets to capture
    packet_limit = int(input(Fore.CYAN + "How many packets do you want to capture? " + Style.RESET_ALL))

    # Start sniffing, stop when the packet limit is reached
    sniff(prn=packet_callback, store=0, stop_filter=stop_sniff)
