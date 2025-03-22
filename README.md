# subdiger Explanation
This tool helps to identify subdomains of a website contains flag "-o" & "-w" to specify output file and to use custom wordlists.
1) First import libraries as per requirement.
2) Then create a banner for better outlook with the text &quot;Tool for Subdomain Enum&quot;
3) After that, checking whether the argument which the domain name has been entered by the user or
not.
4) Now the try block will open the &quot;list.txt&quot; file which contains subdomains like www, mail, blog, api, etc
and run over it. To create the &quot;list.txt&quot; navigate to
https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-
5000.txt, from here copy the names or clone the file. If the &quot;list.txt&quot; doesn&#39;t exists then except block will
execute with the print message.
5) The next try block will execute and the for loop inside will and the variable sub_domain store the
string as shown substituting the &quot;sub&quot; with subdomain and &quot;{sys.argv[1]}&quot; with the entered domain
name by user.

6) Next try block will check for response time if no response receive within 5 seconds will raise a timeout
error and also check for status codes such as 403, 500, 404.
7) Then the next except block will pass it as connection error if neither of the above happens else block
will execute and print the message with valid subdomain as &quot;https://mail.google.com&quot;.
8) If user interrupt or stop the enumeration then the last except block will execute.


**Usage**
python3 sub_domain.py -h                                                                                                   

IF YOU WANT TO STOP THE ENUMERATION PRESS Ctrl+C

 ____        _     ____  _                 
/ ___| _   _| |__ |  _ \(_) __ _  ___ _ __ 
\___ \| | | | '_ \| | | | |/ _` |/ _ \ '__|
 ___) | |_| | |_) | |_| | | (_| |  __/ |   
|____/ \__,_|_.__/|____/|_|\__, |\___|_|   
                           |___/           

usage: sub_domain.py [-h] [-o OUTPUT] [-w WORDLIST] domain

Subdomain Enumeration Script

positional arguments:
  domain                The domain to enumerate subdomains for

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file to save valid subdomains
  -w WORDLIST, --wordlist WORDLIST
                        Custom wordlist file
