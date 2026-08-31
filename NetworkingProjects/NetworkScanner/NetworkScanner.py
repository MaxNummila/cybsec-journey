import ipaddress
import socket
import errno

inputIP = input("Please enter an IP Address: ")


network = ipaddress.ip_network(str(inputIP), strict=False)

ports = [22, 80, 43, 8080]

for port in ports:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.settimeout(1)

    result = (socket_obj.connect_ex((inputIP, port)))
    if result == 0:
        print(f"{inputIP}:{port} is open")
    else:
        print(result)
        print(errno.errorcode.get(result))
    socket_obj.close()
