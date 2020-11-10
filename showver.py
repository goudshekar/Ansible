import os
import sys
import paramiko
import netmiko
from netmiko import ConnectHandler
import getpass

username = input("Username:")
password = getpass.getpass("Password: ")

command = input('Enter you command:')

ipv4 = ['172.17.236.68','172.17.236.69']

for i in ipv4:
    device = {
    'device_type': 'cisco_ios',
    'host':i,
    'username': username,
    'password': password
    }

    net_connect = ConnectHandler(**device) 

    output = net_connect.find_prompt()

    version = net_connect.send_command(command)

    print(output)

    print(version)



#print(type(device))



