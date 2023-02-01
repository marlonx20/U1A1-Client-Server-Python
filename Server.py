import socket

# Definimos la dirección IP de este servidor
SERVER_ADDRESS = '192.168.100.239'

# Definimos el puerto de escucha
SERVER_PORT = 22222

# Creamos el socket
s = socket.socket()

# Esto permite que el programa se reinicie inmediatamente después de una salida.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Asociamos el socket con la dirección IP y el puerto
s.bind((SERVER_ADDRESS, SERVER_PORT))

# Escuchamos hasta 5 clientes
s.listen(5)

print("Escuchando en la dirección %s. Detenga el servidor con Ctrl-C" %
str((SERVER_ADDRESS, SERVER_PORT)))

# Listo, ahora comenzamos a escuchar y capturar los datos que nos envíen los clientes
while True:
    c, addr = s.accept()
    print("\nConexion recibida desde %s" % str(addr))

    while True:
        data = c.recv(2048)
        if not data:
            print("Fin de trasmision desde el cliente. Reiniciando")
            break

# Recibimos información del cliente. Usamos el método decode() porque la información viene en bytes

        data = data.decode()

        print("Inormacion recibida '%s' desde el cliente" % data)

        data = input(">> ")

# Codificamos la respuesta que le vamos a enviar al cliente, en bytes
        data = data.encode()

# Le enviamos la respuesta al cliente.
        c.send(data)

c.close()