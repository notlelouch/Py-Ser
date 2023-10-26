import socket

def handle_request(request_data):
    input_string = request_data.strip()
    parts = input_string.split()

    if parts[1].startswith("/"):
        response_string = parts[1].split("/")
        
        if len(response_string) == 2:
            response = "HTTP/1.1 200 OK\r\n\r\n"
            
        if len(response_string) > 2:
            str_response = parts[1].split("/echo/")
            if len(str_response) == 2:
                final_str_response = str_response[1]
                str_len_response += len(final_str_response)
                response = "HTTP/1.1 200 OK\r\n\r\n Content-Type: text/plain \r\n\r\n Content_length: str_len_response\r\n\r\n final_str_response\r\n\r\n"
            else:
                response = "HTTP/1.1 404 Bad Request\r\n\r\ninvalid request "
        return response
    else:
        response = "HTTP/1.1 404 Bad Request\r\n\r\ninvalid request "
    
    return response
        
    # if request_data.startswith("GET HTTP/1.1"):
    #     response = "HTTP/1.1 200 OK\r\n\r\nHello Aryan!"    
    #     response += " " + response_string
    # else:
    #     response = "HTTP/1.1 404 Bad Request\r\n\r\ninvalid request"
    # return response
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
