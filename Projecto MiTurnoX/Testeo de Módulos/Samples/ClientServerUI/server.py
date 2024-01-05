import socket
import threading
import tkinter as tk

def process_data(data):
    # Placeholder function; replace with your own logic
    print(f"Processing data: {data['message']}")
    if 'task' in data:
        print(f"Task: {data['task']}")

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        decoded_data = data.decode('utf-8')
        data_dict = eval(decoded_data)
        process_data(data_dict)
        client_socket.send("ACK".encode('utf-8'))
    client_socket.close()

class ServerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Server GUI")

        # Text widget to display server logs
        self.log_text = tk.Text(self, height=10, width=40)
        self.log_text.pack(padx=10, pady=10)

        # Start button to start the server
        self.start_button = tk.Button(self, text="Start Server", command=self.start_server)
        self.start_button.pack(pady=10)

        # Stop button to stop the server
        self.stop_button = tk.Button(self, text="Stop Server", command=self.stop_server)
        self.stop_button.pack(pady=5)

        # Initialize server socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(('0.0.0.0', 8888))

        # Flag to indicate whether the server should keep running
        self.server_running = False

    def start_server(self):
        # Set the flag to indicate the server should keep running
        self.server_running = True

        # Start the server in a separate thread
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()

    def stop_server(self):
        # Set the flag to indicate the server should stop running
        self.server_running = False

        # Close the server socket to unblock the accept call
        self.server_thread.close()

    def run_server(self):
        self.server.listen(5)
        self.log_text.insert(tk.END, "[*] Server is listening on 0.0.0.0:8888\n")
        while self.server_running:
            try:
                client, addr = self.server.accept()
                self.log_text.insert(tk.END, f"[*] Accepted connection from: {addr[0]}:{addr[1]}\n")
                client_handler = threading.Thread(target=handle_client, args=(client,))
                client_handler.start()
            except socket.error:
                # Socket error occurs when the server socket is closed
                break

if __name__ == "__main__":
    server_gui = ServerGUI()
    server_gui.mainloop()
