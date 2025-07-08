# Subnet Analysis and Visualization Tool

## Overview
Analyzes IPs and subnet masks, calculates network details, groups by CIDR, generates a JSON report, and visualizes host distribution.

## Requirements
- Python 3.11+
- pip

## Installation
```bash
pip install pandas matplotlib openpyxl
```

## Usage
### Locally
```bash
python subnet_analyzer.py
python visualize.py
```

### With Docker
```bash
docker build -t subnet-analyzer .
docker run -v $PWD:/app subnet-analyzer
```

## Output
- `subnet_report.json`: Generated subnet report
- `network_plot.png`: Bar chart of hosts per subnet

## Files
- `subnet_analyzer.py`: Main processing script
- `visualize.py`: Chart generator (optional)
- `ip_data.xlsx`: Input IP data
- `subnet_report.json`: Output report
- `network_plot.png`: Visualization output
- `report.md`: Answers to analysis questions
- `Dockerfile`: Container definition

## Notes
Ensure `ip_data.xlsx` exists in project root. expected columns are: `IP Address`, `Subnet Mask`.

