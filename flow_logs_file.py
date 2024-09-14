import random
import time

def generate_flow_logs():
    protocols = list(range(0, 143))
    
    # Function to generate a random IP address
    def generate_ip():
        return ".".join(map(str, (random.randint(0, 255) for _ in range(4))))

    # Function to generate a flow log entry
    def generate_flow_log_entry_full_dst_ports():
        version = "2"
        account_id = f"123456789012"
        interface_id = f"eni-{random.randint(10000000,99999999)}"
        srcaddr = generate_ip()
        dstaddr = generate_ip()
        srcport = random.randint(1024, 65535)
        dstport = random.randint(1, 50)  # Random range for destination ports from 1-50
        protocol = random.choice(protocols)
        packets = random.randint(1, 10000)
        bytes_transferred = random.randint(64, 1000000)
        start_time = int(time.time()) - random.randint(0, 3600)
        end_time = start_time + random.randint(1, 60)
        action = random.choice(["ACCEPT", "REJECT"])
        log_status = random.choice(["OK", "NODATA"])
        return f"{version} {account_id} {interface_id} {srcaddr} {dstaddr} {srcport} {dstport} {protocol} {packets} {bytes_transferred} {start_time} {end_time} {action} {log_status}"

    # Generate flow logs
    flow_log_entries_full_dst_ports = [generate_flow_log_entry_full_dst_ports() for _ in range(90000)]

    # Save the generated flow logs to a file
    with open("flow_logs.txt", "w") as file:
        file.write("\n".join(flow_log_entries_full_dst_ports))

    print("Flow logs generated and saved to flow_logs.txt")
