import socket

SERVER_ADDRESS = ('localhost', 53)

records = {
    'hacker.com': '192.168.1.1',
    'www.hacker.com': '192.168.2.1',
    'cyber.hacker.com': 'www.cicra.com'
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(SERVER_ADDRESS)

print(f'DNS server started on {SERVER_ADDRESS}')

while True:
    data, addr = sock.recvfrom(512)
    print(f'Received DNS query from {addr}')

    query = data.decode().split()
    query_type = query[0]
    hostname = ' '.join(query[1:])  

    if hostname in records:
        if query_type == 'A':
            response = f'{hostname} {records[hostname]}'
        elif query_type == 'CNAME':
            response = f'{hostname} {records[hostname]}'
    else:
        response = f'Error: {hostname} not found'

    sock.sendto(response.encode(), addr)
    print(f'Sent DNS response: {response}')
