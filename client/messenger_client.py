import socket

class messenger_client:
    def __init__(self, ip, port):
        # 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
        self.server_ip = ip
        # 서버에서 지정해 놓은 포트 번호입니다.
        self.server_port = port

    def connect(self):
        # 소켓 객체를 생성합니다.
        # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


        # 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
        client_socket.connect((self.server_ip, self.server_port))

        # 메시지를 전송합니다.
        client_socket.sendall('안녕'.encode())

        # 메시지를 수신합니다.
        data = client_socket.recv(1024)
        print('Received', repr(data.decode()))

        # 소켓을 닫습니다.
        client_socket.close()

if __name__ == '__main__':
    client = messenger_client('127.0.0.1', 9999)
    client.connect()