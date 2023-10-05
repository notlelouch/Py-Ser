import socket

def handle_request(request_data):
    if request_data.startswith("GET /index.html"):
        response = "HTTP/1.1 200 OK\r\n\r\nHello Aryan!!"
    else:
        response = "HTTP/1.1 400 Bad Request\r\n\r\nPage not found"
    return response
def main():
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    while True:
        client_socket, client_address = server_socket.accept()# wait for client
        request_data = client_socket.recv(1024).decode("utf-8")
        
        response = handle_request(request_data)

        if response is not None:
            client_socket.send(response.encode("utf-8"))
        client_socket.close()
        
if __name__ == "__main__":
    main()
