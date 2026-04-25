import socket
from datetime import datetime
from colorama import Fore, Style, init

# Initialize colorama #
init()

# Banner #
print(Fore.CYAN + "="*50)
print("        PYTHON PORT SCANNER")
print("="*50 + Style.RESET_ALL)

# Take input #
target = input("Enter target IP or website (e.g. google.com): ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print(Fore.RED + "Invalid target!" + Style.RESET_ALL)
    exit()

print(f"\nScanning target: {target_ip}")
print("Time started:", datetime.now())
print("-"*50)

# Scanning ports #
try:
    for port in range(1, 1025):  # Common ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(Fore.GREEN + f"[OPEN] Port {port}" + Style.RESET_ALL)

        s.close()

except KeyboardInterrupt:
    print("\nScan stopped by user")

except socket.error:
    print(Fore.RED + "Couldn't connect to server" + Style.RESET_ALL)

print("\nScan completed.")