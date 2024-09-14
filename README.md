# Flow Log Analysis Project

This project generates flow logs, protocol mappings, lookup tables, and performs analysis to count the unique tags and port/protocol combinations. The outputs include CSV files containing sorted tag counts and port/protocol combination counts.

Project Structure

The project contains the following files:

## 1. flow_logs_file.py
Key functions:
generate_ip(): Generates a random IP address.
generate_flow_log_entry(): Generates a flow log entry with randomized values.
generate_flow_logs(): The method when called generates 90,000 flow log entries, including details like version, account ID, source and destination IPs, ports, protocol numbers (0-142), packets, bytes transferred, and action status. The flow logs are stored in flow_logs.txt.

## 2. protocol_mapping.py
Key function:
generate_protocol_mapping(): This method when called creates a protocol-to-number mapping for protocols 0 to 142, and saves the mapping to protocol_number_mapping.txt.

Key features:
The protocol mapping dictionary contains standard protocol names mapped to their corresponding numbers.
The script saves the protocol mapping to protocol_number_mapping.txt in the format: protocol_number,protocol_name.

## 3. lookup_table_generation.py
Key function:
generate_lookup_table(): This meyhod when called generates a lookup table with random destination ports, sprotocol names (from protocol_number_mapping.txt), and associated tags. The lookup table is stored in lookup_table.csv.

Key features:
Reads protocol_number_mapping.txt and maps random protocol numbers to their names.
Randomly assigns destination ports (1-50) and tags (sv_P1 to sv_P9, email, web, db).
Generates 10,000 entries and saves them to lookup_table.csv.

## 4. generate_tag_and_port_protocol_count.py

### Generates Required Files:
The script first calls the functions from the other modules:
#### flow_logs_file.py: 
Generates flow_logs.txt, which contains 90,000 flow log entries.
#### protocol_mapping.py: 
Generates protocol_number_mapping.txt, which maps protocol numbers to protocol names.
#### lookup_table_generation.py: 
Generates lookup_table.csv, which contains destination ports, protocol names, and associated tags.

### Merging Flow Logs, Protocol Mapping, and Lookup Table:
The flow logs are merged with:
#### Protocol Mapping: 
Maps the protocol numbers in the flow logs to their human-readable protocol names (e.g., TCP, UDP).
#### Lookup Table: 
Matches the destination port and protocol combination in each flow log to assign a corresponding tag (e.g., sv_P1, web, email).
#### Handling Unmatched Entries:
For flow logs that do not have a corresponding tag (i.e., the combination of destination port and protocol does not exist in the lookup table), the tag is set to "Untagged".
#### Counting Unique Tags and Port/Protocol Combinations:
Tag Count: The script counts how many times each tag appears across all flow logs.
Port/Protocol Combination Count: It also counts unique combinations of destination ports and protocol names.
#### Sorting and Saving Results:
The tag counts and port/protocol combination counts are sorted in descending order.
The sorted results are saved to:
tag_count.csv: Contains the counts of each tag.
port_protocol_count.csv: Contains the counts of each unique destination port/protocol combination.

## 5. sample_lookup_table.csv
A sample lookup table provided for reference. It was used as a basis for generating a more comprehensive lookup table (lookup_table.csv) in the project. You can inspect this file to understand the structure of the lookup table, including the columns for destination ports, protocols, and tags.

# Running the Project

To run this project, you only need to execute the generate_tag_and_port_protocol_count.py script. This script will automatically generate the required files and perform the analysis.

## Mac/Linux
python3 generate_tag_and_port_protocol_counts.py

## Windows
python generate_tag_and_port_protocol_counts.py
