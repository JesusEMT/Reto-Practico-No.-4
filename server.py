#Servidor TCP
import socket
from datetime import date
from datetime import datetime
import os
import platform
host = "localhost"
port = 8888

# hoy = datetime.now()

def fecha_actual(recibdo_c):
    if (recibdo_c=="fecha"):
        hoy = datetime.now()
        mes = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        dia = hoy.day
        mes = mes[hoy.month - 1]
        ano = hoy.year
        msj = "{} de {} del {}".format(dia, mes, ano)
    if (recibdo_c=="hora"):
        hoy = datetime.now()
        hora = hoy.hour
        min  = hoy.minute
        seg = hoy.second
        msj = "{}:{}:{}".format(hora, min, seg)
    return msj

    # def directorios ():
    #     return msj

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen(1)
print("Servidor en espera de conexiones nuevas")
active, addr = server.accept()

while True:
    recibido = active.recv(1024).decode(encoding="ascii", errors="ignore")
    print("cliente: ", recibido)
    if (recibido == "fecha"):
        enviar=("La fecha actual es: ")+fecha_actual(recibido)
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
    elif  (recibido == "hora"):
        enviar=("La hora actual es: ")+fecha_actual(recibido)
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
    elif  recibido == "os":
        enviar = "Informacion del Server: \n\t\t SO :"+ str(platform.system()) + " " + str(platform.release()) + "\n\t\t Arquitectura :" + str(platform.architecture()) +"\n\t\t Procesador :" + str(platform.processor())
        active.send(enviar.encode(encoding = "ascii", errors = "ignore"))
    elif  recibido == "ls":
        enviar = "La lista de todos los archivos y directorios: \n\t" + str(os.listdir())
        active.send(enviar.encode(encoding="ascii",errors="ignore"))
    elif (recibido == "salir"):
        enviar="Saliste del servidor"
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
        break
    elif (recibido == "help"):
        enviar="Comandos especiales :\n\t fecha (muestra hora) \n\t hora  (muestra hora) \n\t os    (muestra info del Server) \n\t ls    (muestra directorios del Server) \n\t salir (Cerrar conexion)"
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
    else:
        enviar=input("server: ")
        active.send(enviar.encode(encoding="ascii", errors="ignore"))
active.close()
