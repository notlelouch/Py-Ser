import socket

def main():
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        client_socket, client_address = server_socket.accept()# wait for client

        request_data = client_socket.recv(1024).decode("utf-8")
        response = "HTTP/1.0 200 OK\r\n\r\nHello Aryan!!"

        client_socket.send(response.encode("utf-8"))
        client_socket.close()
        
if __name__ == "__main__":
    main()
