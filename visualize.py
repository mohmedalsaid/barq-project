import json
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from typing import Dict, List, Tuple, Any

INPUT_FILE = 'subnet_report.json'
OUTPUT_PLOT_FILE = 'network_plot.png'

def load_data(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"error: file at '{file_path}' cannot be found.")
        print("first run 'python subnet_analyzer.py' to generate the desired report")
        exit()
    except json.JSONDecodeError:
        print(f"error: Could not decode JSON file from '{file_path}'. there is aproblem with the file")
        exit()

def process_data(data: List[Dict[str, Any]]) -> List[Tuple[str, int]]:
    host_counts: Dict[str, int] = {}
    for entry in data:
        subnet_id = f"{entry['Network']}{entry['CIDR']}"
        host_counts[subnet_id] = entry['Usable Hosts']

    return sorted(host_counts.items(), key=lambda item: item[1], reverse=True)

def create_plot(sorted_subnets: List[Tuple[str, int]]):
    """Creates, saves, and displays the bar chart."""
    if not sorted_subnets:
        print("No subnet data to plot.")
        return
    subnets, hosts = zip(*sorted_subnets)
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = cm.viridis(np.linspace(0, 1, len(subnets)))
    bars = ax.bar(subnets, hosts, color=colors)

    ax.bar_label(bars, padding=3)

    #  labels , titles 
    ax.set_xlabel('Subnet (Network Address/CIDR)')
    ax.set_ylabel('Number of Usable Hosts')
    ax.set_title('Usable Hosts per Subnet')

    ax.set_ylim(top=ax.get_ylim()[1] * 1.1)

    plt.xticks(rotation=45, ha='right')
    fig.tight_layout()  

    plt.savefig(OUTPUT_PLOT_FILE)
    print(f"img is saved to {OUTPUT_PLOT_FILE}")
    plt.show()

def main():
    report_data = load_data(INPUT_FILE)
    processed_data = process_data(report_data)
    create_plot(processed_data)

if __name__ == "__main__":
    main()
