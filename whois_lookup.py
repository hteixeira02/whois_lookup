import whois
import re
import json
from datetime import datetime

def is_valid_domain(domain):
    pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$"
    return re.match(pattern, domain)

def save_to_txt(domain, data):
    filename = f"whois_{domain}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(data)
    print(f"[INFO] TXT file saved: {filename}")

def save_to_json(domain, data):
    filename = f"whois_{domain}.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, default=str)
    print(f"[INFO] JSON file saved: {filename}")

def whois_lookup(domain):
    try:
        result = whois.whois(domain)

        if not result or not result.text:
            print("[NO DATA] No WHOIS information found.")
            return

        print("\n=== WHOIS INFORMATION ===\n")
        print(result.text)

        save_to_txt(domain, result.text)
        save_to_json(domain, dict(result))

    except whois.parser.PywhoisError:
        print("[ERROR] Invalid domain or no WHOIS data available.")
    except Exception as e:
        print(f"[UNKNOWN ERROR] {e}")

def main():
    domain = input("Target: ").strip().lower()

    if not is_valid_domain(domain):
        print("[ERROR] Invalid domain format.")
        return

    whois_lookup(domain)

if __name__ == "__main__":
    main()
