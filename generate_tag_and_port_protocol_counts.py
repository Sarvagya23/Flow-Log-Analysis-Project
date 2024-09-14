import csv
from collections import defaultdict
from flow_logs_file import generate_flow_logs
from protocol_mapping import generate_protocol_mapping
from lookup_table_generation import generate_lookup_table

# Generate the necessary files before processing
generate_flow_logs()
generate_protocol_mapping()
generate_lookup_table()

# Function to read a file into a list of dictionaries, with customizable delimiter
def read_file(file_path, headers, delimiter):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=delimiter)
        for row in csv_reader:
            data.append(dict(zip(headers, row)))
    return data

# Load lookup_table.csv
lookup_table_path = "lookup_table.csv"
lookup_headers = ["dst_port", "protocol", "tag"]
lookup_table = read_file(lookup_table_path, lookup_headers, delimiter=",")

# Load protocol_number_mapping.txt
protocol_mapping_path = "protocol_number_mapping.txt"
protocol_mapping_headers = ["protocol_number", "protocol_name"]
protocol_mapping = read_file(protocol_mapping_path, protocol_mapping_headers, delimiter=",")

# Load flow_logs.txt
flow_logs_path = "flow_logs.txt"
flow_logs_headers = [
    "version", "account_id", "interface_id", "srcaddr", "dstaddr", 
    "srcport", "dstport", "protocol_number", "packets", "bytes", 
    "start_time", "end_time", "action", "log_status"
]

flow_logs = read_file(flow_logs_path, flow_logs_headers, delimiter=" ")

# Convert protocol_number to int in both flow_logs and protocol_mapping and lowercase protocol names
protocol_mapping_dict = {int(entry['protocol_number']): entry['protocol_name'].lower() for entry in protocol_mapping}

# Convert lookup table to a dictionary with (dst_port, protocol_name) as key
lookup_table_dict = {(entry['dst_port'], entry['protocol'].lower()): entry['tag'] for entry in lookup_table}

# Process flow logs
for log in flow_logs:
    log['protocol_number'] = int(log['protocol_number'])
    log['protocol_name'] = protocol_mapping_dict.get(log['protocol_number'], "unknown")
    log['tag'] = lookup_table_dict.get((log['dstport'], log['protocol_name']), "Untagged")

# Count occurrences of each tag
tag_count = defaultdict(int)
for log in flow_logs:
    tag_count[log['tag']] += 1

# Count unique port/protocol combinations
port_protocol_count = defaultdict(int)
for log in flow_logs:
    key = (log['dstport'], log['protocol_name'])
    port_protocol_count[key] += 1

# Sort the tag counts in descending order
sorted_tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)

# Sort the port/protocol combinations in descending order
sorted_port_protocol_count = sorted(port_protocol_count.items(), key=lambda x: x[1], reverse=True)

# Save the sorted tag count to CSV
with open("tag_count.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["tag", "count"])
    for tag, count in sorted_tag_count:
        writer.writerow([tag, count])

# Save the sorted port/protocol count to CSV
with open("port_protocol_count.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["dst_port", "protocol_name", "count"])
    for (dst_port, protocol_name), count in sorted_port_protocol_count:
        writer.writerow([dst_port, protocol_name, count])

print("CSV files generated.")
