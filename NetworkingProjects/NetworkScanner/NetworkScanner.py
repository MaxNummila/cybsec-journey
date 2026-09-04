import ipaddress
import socket
import errno

inputIP = input("Please enter an IP Address: ")
network = ipaddress.ip_network(str(inputIP), strict=False)
ports = [22, 80, 43, 8080]

for port in ports:
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.settimeout(2)

    try:
        socket_obj.connect((str(inputIP), port))
        print(f"{inputIP}:{port} is open")
    except socket.timeout:
        print(f"{inputIP}:{port} timed out")

    except ConnectionRefusedError:
        print(f"{inputIP}:{port} connection refused")

    except OSError as e:
        print(f"{inputIP}:{port} failed: {e}")

    finally:
        socket_obj.close()
