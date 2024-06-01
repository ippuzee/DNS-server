import socket

SERVER_ADDRESS = ('localhost', 53)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    hostname = input('Enter hostname/alias or "exit" :')

    if hostname.lower() == 'exit':
        break

    #Construct the DNS query
    query = f'A {hostname}'

    #Send the DNS query to the server
    sock.sendto(query.encode(), SERVER_ADDRESS)
    print(f'Sent DNS query: {query}')

    #Receive the DNS response from the server
    data, addr = sock.recvfrom(512)
    response = data.decode()
    print(f'Received DNS response: {response}')

sock.close()
