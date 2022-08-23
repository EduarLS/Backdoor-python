import socket
import sys
   
ser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
puerto = 9999
buffersize = 5000 
ser.bind((host, puerto))
ser.listen(1)

while True:
    print("ESPERANDO CONEXION. . .")
    cliente, direccion = ser.accept()
    print("SE ESTABLECIO CONEXION {0}".format(direccion[0]))
    print("Para descargar imagenes usar \ncomando: extrae, se guardan con el mismo nombre del cliente.\ncomando: exit, se cierra conexion del cliente.\ncomando: quit, se cierra servidor.")
    while True:
        try:
            comando = input("\nIngrese el comando a ejecutar: \n>>")
            cliente.sendall(comando.encode())
            if comando == "": pass
            elif (comando == "exit"):
                pass
            elif(comando == "extrae"):
                directorio  = cliente.recv(buffersize)
                print(directorio.decode())
                archivo = input("\nIngrese el nombre del archivo a descargar junto con su extension: \n>> ")
                cliente.send(archivo.encode())
                mensaje = cliente.recv(buffersize).decode()
                if mensaje.count("ERROR"):
                    pass
                else: 
                    with open (archivo, 'wb') as x:
                        contenido = cliente.recv(buffersize)
                        x.write(contenido)
                        print(mensaje)
                        pass
                        x.close()
            elif comando[:2].lower() == "cd":
                output = cliente.recv(buffersize)
                print(output.decode())
                pass
            elif comando == 'quit':
                quit()
            else:
                output = cliente.recv(buffersize)
                print(output.decode())
        except Exception:
            break
