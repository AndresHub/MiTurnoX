import socket
import json


def start_client():
    # Create a socket using IPv4 and TCP/IP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server at the specified IP address and port
    client.connect(('127.0.0.1', 8888))

    while True:
        # Prompt the user to enter a message and additional parameters
        message = input("Enter message: ")
        task = input("Enter task: ")

        # Create a dictionary containing the message and additional parameters
        data = {'message': message, 'task': task}
        
        # Convert the dictionary to a JSON string
        json_data = json.dumps(data)

        # Send the JSON-encoded data to the server
        client.send(json_data.encode('utf-8'))

        # Receive and print the acknowledgment from the server
        response = client.recv(1024)
        print(f"Server Response: {response.decode('utf-8')}")

    # Close the connection with the server when the loop exits
    client.close()


# Call the start_client function to initiate communication with the server
start_client()
