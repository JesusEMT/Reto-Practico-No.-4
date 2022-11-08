#Cliente TCP
import socket
host = "localhost"
port = 8888

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((host,port))
print("Inicializando cliente")
print("Comandos especiales: fecha, hora, os, ls, salir, help")

while True:
    enviar = input("Cliente: ")
    # print = type(enviar)
    socket1.send(enviar.encode(encoding="ascii", errors="ignore"))
    recibido = socket1.recv(1024)
    print("servidor: ", recibido.decode(encoding="ascii", errors="ignore"))

socket1.close()
