import socket

def Main():
    host = '127.0.0.1'
    port = 12346
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    mensaje = "tu ptm, mtp ut"
    while True:
        s.send(mensaje.encode("utf-8"))
        data = s.recv(1024)
        print("recivido", str(data.decode("utf-8")))
        ans = input("sigues?")
        if ans == "y":
            continue
        else:
            break
    s.close()

if __name__ == "__main__":
    Main()