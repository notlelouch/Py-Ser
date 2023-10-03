import socket

def main():
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Logs from your program will appear here!")

    while True:
        client_socket, client_address = server_socket.accept()# wait for client

        request_data = client_socket.recv(1024).decode("utf-8")
        response = "HTTP/1.0 200 OK\r\n\r\nHello Aryan!! and duniya ki ma ki chutttt!!"
        #response = "HTTP/1.0 200 OK\r\n\r\n duniya ki ma ki chutttttttt!!!!!!!!"

        print("ig it worked somehow, i really don't undertand it much yet")
        client_socket.send(response.encode("utf-8"))
        client_socket.close()
        
if __name__ == "__main__":
    main()
