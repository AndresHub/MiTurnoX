import socket
import threading

def process_data(data):
    # This is a placeholder function; you can replace it with your own logic
    print(f"Processing data: {data['message']}")
    # Extract additional parameters
    if 'task' in data:
        print(f"Task: {data['task']}")

# Function to handle communication with each connected client
def handle_client(client_socket):
    while True:
        # Receive data from the client (up to 1024 bytes)
        data = client_socket.recv(1024)
        if not data:
            # If no data is received, the client has disconnected
            break
        # Decode the received data as JSON
        decoded_data = data.decode('utf-8')
        # Convert the JSON string to a Python dictionary
        data_dict = eval(decoded_data)  # Note: This is a simple example; consider using a proper JSON library
        # Pass the received data to the process_data function
        process_data(data_dict)
        # Send an acknowledgment back to the client
        client_socket.send("ACK".encode('utf-8'))
    # Close the connection with the client when the loop exits
    client_socket.close()


# Function to start the server
def start_server():
    # Create a socket using IPv4 and TCP/IP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a specific IP address and port
    server.bind(('0.0.0.0', 8888))
    # Listen for incoming connections with a maximum queue size of 5
    server.listen(5)

    print("[*] Listening on 0.0.0.0:8888")

    while True:
        # Accept a connection from a client
        client, addr = server.accept()
        print(f"[*] Accepted connection from: {addr[0]}:{addr[1]}")

        # Create a new thread to handle the client's communication
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


# Call the start_server function to begin listening for connections
start_server()