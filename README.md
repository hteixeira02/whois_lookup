# WHOIS Lookup Tool (Python)

Python tool for performing WHOIS lookups and exporting domain registration data in structured formats.

## Description
This project performs WHOIS queries to retrieve public domain registration information, supporting studies in cybersecurity, OSINT, and domain reconnaissance.

The tool outputs the raw WHOIS response to the terminal and saves the results in both TXT and JSON formats for further analysis.

## Features
- WHOIS lookup for target domains
- Input validation for domain names
- Error handling for invalid or unavailable WHOIS data
- Output displayed in terminal
- Export results to:
  - TXT (raw WHOIS response)
  - JSON (structured data)

## Requirements
- Python 3.x
- python-whois

## Installation
```bash
pip install python-whois
```
## Usage 
```bash
python whois_lookup.py
```
