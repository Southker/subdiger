import requests
import sys
import pyfiglet

print("\n\n")
print("IF YOU WANT TO STOP THE ENUMERATION PRESS Ctrl+C")
print("\n\n")

banner = pyfiglet.figlet_format("SubDiger")
print(banner)

if len(sys.argv) == 1:
    print("Usage: python script.py <domain>")
    sys.exit(1)

try:
    with open("list.txt", "r") as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print("list.txt not found!")
    sys.exit(1)

try:
    for sub in subdomains:
        sub_domain = f"https://{sub}.{sys.argv[1]}"
    try:
        response = requests.get(sub_domain, timeout=5)
        response.raise_for_status()
    except requests.ConnectionError:
        pass
    else:
        print("Valid Domain:", sub_domain)

except KeyboardInterrupt:
    print("\nEnumeration stopped. Interrupted with keyboar")
    sys.exit(0)
