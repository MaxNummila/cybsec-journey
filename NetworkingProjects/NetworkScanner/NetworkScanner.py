import ipaddress
import socket

inputIP = input("Please enter an IP Address: ")


network = ipaddress.ip_network(str(inputIP), strict=False)

ports = [22, 80, 43, 8080]

socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.setdefaulttimeout(1)

for port in ports:
    print(socket_obj.connect_ex((inputIP, port)))

socket_obj.close()
