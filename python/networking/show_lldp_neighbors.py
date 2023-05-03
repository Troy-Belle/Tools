from netmiko import ConnectHandler
from getpass import getpass

# Prompt user for IP addresses/hostnames
devices = input("Enter one or more IP addresses/hostnames (separated by commas): ")
device_list = devices.split(",")

# Prompt user for login credentials
username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Loop through devices and connect to each one
for device in device_list:
    device_info = {
        "device_type": "cisco_xe",  # Use cisco_xe for IOS XE 16.10 and later
        "ip": device.strip(),
        "username": username,
        "password": password,
    }

    # Connect to device and run command
    with ConnectHandler(**device_info) as net_connect:
        output = net_connect.send_command("show lldp neighbors")
        print(f"\n\n{'='*50}\n{device}:\n{'='*50}\n{output}")
