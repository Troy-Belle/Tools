import subprocess
import time
from prettytable import PrettyTable
import sys

ip_list = input("Enter a comma-separated list of IP addresses: ")
ips = ip_list.replace(" ", "").split(",")  # Remove any spaces and split the string into a list
interval = int(input("Enter the desired interval between pings (in seconds): "))

table = PrettyTable()
table.field_names = ["IP Address", "Status"]

while True:
    table.clear_rows()
    for ip in ips:
        process = subprocess.Popen(["fping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            table.add_row([ip, "alive"])
        else:
            table.add_row([ip, stderr.decode('utf-8').strip()])
        print(table)
        sys.stdout.flush()
    time.sleep(interval)