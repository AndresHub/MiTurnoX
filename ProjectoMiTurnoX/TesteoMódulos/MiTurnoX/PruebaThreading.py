import threading
import socket
from config import config

IP = socket.gethostbyname(socket.gethostname())
PORT = 54321
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = ("utf-8")
MSG_DISCONNECT = "DISCONNECT"

def modulo(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == MSG_DISCONNECT:
            connected = False
        print(f"[{addr}] {msg}")
        reply = f"[RECIEVED] {msg}"
        conn.send(reply.encode(FORMAT))
    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = modulo, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    main()

"""
def threaded(c):
    while True:
        data = c.recv(1024)
        if not data:
            print_lock.release()
            break
        data = data[::-1]
        c.send(data)
    c.close()

def server_on():
    host = ""
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded a", port)
    s.listen(5)
    print("socket escuchando")
    while True:
        c, addr = s.accept()
        print_lock.acquire()
        print("conectado a", addr[0], " ", addr[1])
        start_new_thread(threaded, (c,))
    s.close()

def server_thread():
    print_lock1.acquire()
    hilo_server = threading.Thread(target=server_on)
    hilo_server.start()
"""