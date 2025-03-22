import requests
import sys
import pyfiglet
import argparse

# Print banner
print("\n\n")
print("IF YOU WANT TO STOP THE ENUMERATION PRESS Ctrl+C")
print("\n\n")

banner = pyfiglet.figlet_format("SubDiger")
print(banner)

# Parse arguments
parser = argparse.ArgumentParser(description='Subdomain Enumeration Script')
parser.add_argument('domain', help='The domain to enumerate subdomains for')
parser.add_argument('-o', '--output', help='Output file to save valid subdomains', default=None)
parser.add_argument('-w', '--wordlist', help='Custom wordlist file', default='list.txt') 

args = parser.parse_args()

# Check for domain argument
if not args.domain:
    print("Usage: python script.py <domain> [-o output_file]")
    sys.exit(1)

# Try to open the subdomain list (either from the custom wordlist or the default list.txt)
try:
    with open(args.wordlist, "r") as file:
        subdomains = file.read().splitlines()
except FileNotFoundError:
    print(f"Wordlist file {args.wordlist} not found!")
    sys.exit(1)

# Prepare output file if specified
output_file = None
if args.output:
    try:
        output_file = open(args.output, 'w')
    except IOError:
        print(f"Error opening output file: {args.output}")
        sys.exit(1)

# Start enumeration
try:
    for sub in subdomains:
        sub_domain = f"https://{sub}.{args.domain}"
        try:
            response = requests.get(sub_domain, timeout=5)
            response.raise_for_status()
        except requests.ConnectionError:
            pass
        else:
            # Write to output file if specified
            valid_domain_message = f"Valid Domain: {sub_domain}"

            if output_file:
                print(f"Results are saving in {args.output}")
                output_file.write(valid_domain_message + '\n')
            else:
                print(valid_domain_message)

except KeyboardInterrupt:
    print("\nEnumeration stopped. Interrupted with keyboard")
    sys.exit(0)

# Close the output file if it was opened
if output_file:
    output_file.close()
