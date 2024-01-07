import socket
import tkinter as tk
from tkinter import messagebox

class ClientGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Client GUI")

        # Entry widgets for message and task
        self.message_entry = tk.Entry(self, width=30)
        self.message_entry.pack(pady=5)
        self.task_entry = tk.Entry(self, width=30)
        self.task_entry.pack(pady=5)

        # Send button to send data to the server
        self.send_button = tk.Button(self, text="Send Data", command=self.send_data)
        self.send_button.pack(pady=10)

        # Initialize client socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('127.0.0.1', 8888))

    def send_data(self):
        # Get message and task from entry widgets
        message = self.message_entry.get()
        task = self.task_entry.get()

        # Check if message is empty
        if not message:
            messagebox.showwarning("Warning", "Message cannot be empty!")
            return

        # Create a dictionary containing message and task
        data = {'message': message, 'task': task}

        # Convert the dictionary to a JSON string
        json_data = str(data)

        # Send the JSON-encoded data to the server
        self.client.send(json_data.encode('utf-8'))

        # Receive and print the acknowledgment from the server
        response = self.client.recv(1024)
        print(f"Server Response: {response.decode('utf-8')}")

if __name__ == "__main__":
    client_gui = ClientGUI()
    client_gui.mainloop()
