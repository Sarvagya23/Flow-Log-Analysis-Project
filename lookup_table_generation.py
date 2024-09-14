import random

def generate_lookup_table():
    # Initialize an empty dictionary to store the protocol number to protocol name mapping
    protocol_number_mapping = {}

    # Read the protocol_number_mapping.txt to populate the dictionary
    with open("protocol_number_mapping.txt", "r") as file:
        for line in file:
            # Each line is expected to be in "number,protocol_name" format
            number, protocol_name = line.strip().split(",")
            protocol_number_mapping[int(number)] = protocol_name.lower()

    # Generating random entries for dstport, protocol (name from mapping), and tag values
    protocols = list(protocol_number_mapping.keys())  
    tags = ["sv_P" + str(i) for i in range(1, 10)] + ["email", "web", "db"]  

    # Function to generate random dstport, protocol (from mapping), and tag values
    def generate_random_lookup_entry():
        dstport = random.randint(1, 50)  # Random port between 1 and 50
        protocol_number = random.choice(protocols)  # Random protocol number from available ones
        protocol_name = protocol_number_mapping[protocol_number]  # Get protocol name
        tag = random.choice(tags)  # Random tag from the list
        return f"{dstport},{protocol_name},{tag}"

    # Generate 10000 new random entries
    lookup_entries = [generate_random_lookup_entry() for _ in range(10000)]

    # Save the generated entries to a .csv file
    with open("lookup_table.csv", "w") as file:
        file.write("\n".join(lookup_entries))

    print("Lookup table generated and saved to lookup_table.csv")