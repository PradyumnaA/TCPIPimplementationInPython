import socket

def main():
    # Create a server socket, bind to a port, and listen for a connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 4000))
    server_socket.listen(1)
    print("Server ready for connection")
    
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print("Connection is successful")

    # Read the file name from the client
    fname = client_socket.recv(1024).decode()
    
    try:
        # Open and read the file contents
        with open(fname, 'r') as file:
            # Send the contents of the file to the client
            for line in file:
                client_socket.sendall(line.encode())
    except FileNotFoundError:
        print(f"File {fname} not found.")
        client_socket.sendall(b"File not found")

    # Close the sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
