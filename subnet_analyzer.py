import pandas as pd
import ipaddress
import json
import sys
from typing import Dict, Any, List

INPUT_FILE = 'ip_data.xlsx'
OUTPUT_FILE = 'subnet_report.json'


def read_ip_data(file_path: str) -> pd.DataFrame:

    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"error: file '{file_path}' not found")
        sys.exit(1)
        
    required_columns = ['IP Address', 'Subnet Mask']
    if not all(col in df.columns for col in required_columns):
        print(f"Error: file must contain the columns: {', '.join(required_columns)}")
        sys.exit(1)
    return df


def analyze_subnets(df: pd.DataFrame) -> List[Dict[str, Any]]:

    subnets: Dict[str, Dict[str, Any]] = {}

    for _, row in df.iterrows():
        ip_str = row['IP Address']
        mask_str = row['Subnet Mask']

        try:
            interface = ipaddress.IPv4Interface(f"{ip_str}/{mask_str}")
            network = interface.network
            network_id = str(network)  
        except ValueError:
            print(f"Warning: Skipping invalid entry: IP '{ip_str}', Mask '{mask_str}'")
            continue

        if network_id not in subnets:
            usable_hosts = network.num_addresses - 2 if network.prefixlen < 31 else 0
            subnets[network_id] = {
                'Network': str(network.network_address),
                'CIDR': f"/{network.prefixlen}",
                'Subnet Mask': str(network.netmask),
                'Broadcast': str(network.broadcast_address),
                'Usable Hosts': usable_hosts,
                'IPs': []  
            }

        subnets[network_id]['IPs'].append(ip_str)

    sorted_subnet_ids = sorted(subnets.keys(), key=ipaddress.ip_network)
    return [subnets[net_id] for net_id in sorted_subnet_ids]


def main():
    ip_data_df = read_ip_data(INPUT_FILE)
    subnet_report = analyze_subnets(ip_data_df)
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(subnet_report, f, indent=4)
    print(f"Subnet analysis report is saved to '{OUTPUT_FILE}'")


if __name__ == "__main__":
    main()

