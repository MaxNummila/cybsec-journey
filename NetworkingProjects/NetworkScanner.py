import ipaddress

inputIP = input("Please enter an IP Address: ")
inputSubnet = input("Please enter a subnet mask: ")

network = ipaddress.ip_network(str(inputIP) + '/' + str(inputSubnet), strict=False)
print(network)
print(network.network_address)
print(network.broadcast_address)

for host in network.hosts():
    print(host)
