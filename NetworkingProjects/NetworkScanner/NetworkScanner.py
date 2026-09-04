import ipaddress
import socket

inputIP = input("Please enter an IP Address: ")
network = ipaddress.ip_network(str(inputIP + '/24'), strict=False)
ports = [22, 80, 43, 8080]

for host in network.hosts():
    if ipaddress.ip_address(host) in network:
        for port in ports:
            socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_obj.settimeout(2)

            try:
                socket_obj.connect((str(host), port))
                print(f"{host}:{port} is open")
            except socket.timeout:
                print(f"{host}:{port} timed out")

            except ConnectionRefusedError:
                print(f"{host}:{port} connection refused")

            except OSError as e:
                print(f"{host}:{port} failed: {e}")

            finally:
                socket_obj.close()

