import socket

# Información de red para conectarse al servidor
SERVER_ADDRESS = '192.168.100.239'
SERVER_PORT = 22222

# Creamos el socket
c = socket.socket()

#Nos conectamos al servidor
c.connect((SERVER_ADDRESS, SERVER_PORT))

# Comenzamos a enviar información al servidor desde nuestro teclado
try:
    input = raw_input
except NameError:
    pass

print("Conectado al servidor: " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        data = input(">> ")
    except EOFError:
        print("\nSayonara...")
        break

    if not data:
        print("Ingrese mensaje antes")
        print("Ctrl-D [or Ctrl-Z en Windows] para salir")
        continue

# Convertimoslos datos en bytes. (solo para Python 3)
    data = data.encode()

# Enviamos
    c.send(data)

# Recibimos respuesta desde el servidor
    data = c.recv(2048)
    if not data:
        print("Server abended. Exiting")
        

# Convertimos la respuesta en un string
    data = data.decode()
    print("<SERVER>")
    print(data + '\n')

c.close()