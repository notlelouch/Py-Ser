import socket

def main():
    print("Logs from your program will appear here!")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(1)

    print("Server listening on port 8080")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Read the HTTP request from the client
        request_data = client_socket.recv(1024).decode("utf-8")

        # Respond with a 200 OK HTTP response
        response = "HTTP/1.1 200 OK\r\n\r\nHello, World!"
        client_socket.send(response.encode("utf-8"))

        client_socket.close()

if __name__ == "__main__":
    main()
