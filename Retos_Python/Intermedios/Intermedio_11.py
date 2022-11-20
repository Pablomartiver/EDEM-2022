'''
Una empresa quiere gestionar su cartera de clientes. Escribe un programa que guarde los clientes en un diccionario u objeto literal en el que disponga de:
NIF (string)
nombre (string)
apellidos (string)
teléfono (string)
email (string)
preferente (boolean)
El programa debe mostrar las siguientes opciones para que escoja el usuario:
Añadir un cliente
Eliminar cliente por NIF
Mostrar Cliente por NIF
Listar TODOS os clientes
Mostrar ÚNICAMENTE los clientes preferentes
Finalizar Programa
'''

def programa ():
  #Creamos la lista clientes y unos clientes para comprobar que todas las funciones van
  cliente1 = {
    "NIF": "12344321G",
    "Nombre": "Carlos",
    "Apellidos": "García Nuñez",
    "Email": "carlos@gmail.com",
    "Telefono": "645723472",
    "Preferente": True,
  }
  cliente2 = {
     "NIF": "56788765K",
    "Nombre": "Maria",
    "Apellidos": "Martínez Riaza",
    "Email": "maria@gmail.com",
    "Telefono": "654736453",
    "Preferente": False,
  }
  cliente3 = {
    "NIF": "38473827H",
    "Nombre": "Ana",
    "Apellidos": "Fernandez Moreno",
    "Email": "ana@gmail.com",
    "Telefono": "687392733",
    "Preferente": False,
  }
  clientes = [cliente1, cliente2, cliente3,]
  

  #Mostramos las diferentes funciones
  print ("Seleccione la funcion que quiere realizar: \n 1- Añadir un cliente \n 2- Eliminar cliente por NIF \n 3- Mostrar cliente por NIF \n 4- Listar TODOS os clientes \n 5- Mostrar ÚNICAMENTE los clientes preferentes \n 6- Finalizar Programa")
  funcion = int(input("Introduce la eleccion que quiere realizar: "))

  #Función añadir un cliente
  if funcion == 1:

    NIF = str(input("Introduce el NIF: "))
    nombre = str(input("Introduce el nombre: "))
    apellidos = str(input("Introduce los apellidos: "))
    email = str(input("Introduce tu email: "))
    telefono = str(input("Introduce tu telefono:"))
    preferente = bool(input("El cliente es preferente (True/False): "))

    nuevo_cliente = {
      "NIF": NIF,
      "Nombre": nombre,
      "Apellidos": apellidos,
      "Email": email,
      "Telefono": telefono,
      "Preferente": preferente,
    }
    clientes.append(nuevo_cliente)
    funcion = int(input("Introduzca una nueva funcion o finalice el programa: "))

  #Función eliminar un cliente por el NIF
  elif funcion == 2:
    nif = str(input("Introduzca el dni del cliente que quiere eliminar:"))
    for i in clientes:
      if i["NIF"] == nif:
        clientes.remove(i)
        print ("El cliente ha sido eliminado.")
        funcion = int(input("Introduzca una nueva funcion o finalice el programa: "))
      else:
        print ("El NIF introducido no corresponde a ningún cliente.")
        
  #Función mostrar cliente por NIF
  elif funcion == 3:
    nif = str(input("Introduzca el NIF para mostrar los datos del cliente:"))
    for i in clientes:
      if i["NIF"] == nif:
        print (f' NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telefono: {i["Telefono"]}, Email: {i["Email"]}, Preferente: {i["Preferente"]}')
        funcion = int(input("Introduzca una nueva funcion o finalice el programa: "))
      else:
        print ("El NIF introducido no corresponde a ningun cliente.")

  #Función listar todos los clientes
  elif funcion == 4:
    for idx, i in enumerate (clientes):
      print (f' NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telefono: {i["Telefono"]}, Email: {i["Email"]}, Preferente: {i["Preferente"]}')
      funcion = int(input("Introduzca una nueva funcion o finalice el programa: "))

  #Función mostrar solo los clientes preferentes
  elif funcion == 5:
    for i in clientes:
      if i["Preferente"] == True:
        print (f' NIF: {i["NIF"]}, Nombre: {i["Nombre"]}, Telefono: {i["Telefono"]}, Email: {i["Email"]}, Preferente: {i["Preferente"]}')
        funcion = int(input("Introduzca una nueva funcion o finalice el programa: "))
      else:
        break

  #Función de cerrar el programa
  elif funcion == 6:
    print ("El programa ha finalizado")
    
     

  #Comprobamos que el usuario no escoga una función que no existe
  else:
    print ("La funcion selecionada no existe.")
    funcion = int(input("Introduzca una funcion que exista por favor: "))

programa ()
