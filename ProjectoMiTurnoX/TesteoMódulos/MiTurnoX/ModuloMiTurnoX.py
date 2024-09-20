import socket

def Main():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 54321
    ADDR = (HOST, PORT)
    SIZE = 1024
    FORMAT = "utf-8"
    MSG_DISCONNECT = "DISCONNECT"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {HOST}:{PORT}")
    connected = True
    while connected:
        msg = input("[TYPE A MESAGE] >")
        client.send(msg.encode(FORMAT))
        if msg == MSG_DISCONNECT:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[MESSAGE RECIEVED] > {msg}")
        



    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    mensaje = "tu ptm, mtp ut"
    while True:
        s.send(mensaje.encode("utf-8"))
        data = s.recv(1024)
        print("recibido", str(data.decode("utf-8")))
        ans = input("sigues?")
        if ans == "y":
            continue
        else:
            break
    s.close()
"""


if __name__ == "__main__":
    Main()