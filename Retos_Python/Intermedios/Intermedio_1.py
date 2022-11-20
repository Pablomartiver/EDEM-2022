#Primero creamos una varibale diccionario para cada género de musica. Luego creamos una lista con todas los tipos de genero. Blacn_metal y electro tienen un descuento del 30%. Primero mostrar por pantalla la lista de gneros, y luego preguntar cual quiere. Cuando lo escoge y presione 0, se debe mostrar el ticket indicando la fecha de compra (datetime), el dinero que se ahorra el usuario y el coste final de la compra

from datetime import datetime
def tienda_discos ():
  #Cremaos una lista que contenga dentro todos los discos, en forma de diccionario
  discos_disponibles = [ 
    {"nombre" : "A", "artista" : "Alberto", "año" : 1998, "precio" : 100, "genero" : "pop"},
    {"nombre" : "B", "artista" : "Borja", "año" : 1999, "precio" : 100, "genero" : "electro"},
    {"nombre" : "C", "artista" : "Carlos", "año" : 2000, "precio" : 100, "genero" : "reggaeton"},
    {"nombre" : "D", "artista" : "Diego", "año" : 2001, "precio"  : 100, "genero" : "rock"},
    {"nombre" : "E", "artista" : "Elena", "año" : 2002, "precio" : 100, "genero" : "metal"},
    {"nombre" : "F", "artista" : "Fran", "año" : 2003, "precio" : 100, "genero" : "death_metal"},
    {"nombre" : "G", "artista" : "Gonzalo", "año" : 2004, "precio" : 100, "genero" : "black_metal"},
  ]
  print ("Estos son los discos disponibles:")
  #Enumeramos los discos para que el cliente los puede escoger 
  for idx,disco in enumerate (discos_disponibles):
    print(f'Num disco {idx+1}: Nombre: {disco["nombre"]} Precio: {disco["precio"]} Genero: {disco["genero"]}')

  print ("Pulsa la tecla 0 para finalizar la compra")
  eleccion = int (input ("Introduce el numero del disco que quieres comprar: "))
  importe = 0
  ahorro = 0
  while eleccion != 0:
    #Eleccion del disco electro y calculamos su importe y descuento
    if eleccion == 2: 
      for i in discos_disponibles:
        for key in i:
          if (key =="genero" and i[key] == "electro"):
            ahorro += (i["precio"]*0.3)
            importe += (i["precio"]) - (i["precio"]*0.3)
            print ("El disco seleccionado tiene un descuento del 30%")
            eleccion = int (input("Seleccione otro disco para añadirlo a la cesta o pulse 0 para acabar la compra: "))

    #Eleccion del disco black_metal y calculamos su importe y descuento
    elif eleccion == 7: 
      for i in discos_disponibles:
        for key in i:
          if (key == "genero" and i[key] == "black_metal"):
            ahorro += (i["precio"])*0.3
            importe += (i["precio"]) - (i["precio"]*0.3)
            print ("El disco seleccionado tiene un descuento del 30%")
            eleccion = int (input("Seleccione otro disco para añadirlo a la cesta o pulse 0 para acabar la compra: "))

    #Comprobamos que el cliente no se equivoque en la eleccion de los discos
    elif eleccion > 7 or eleccion < 0: 
      eleccion = int (input ("El numero de disco seleccionado no existe, seleccione otro numero de disco por favor: "))

    #Calculamos el importe para el resto de discos que no tienen descuento
    else: 
      importe += (discos_disponibles[eleccion] ["precio"])
      eleccion = int (input("Añada otro disco a la cesta o pulse 0 para acabar la compra: "))
  else:
    #Sacamos el ticket del cliente, con la fecha, precio total y descuento 
    print ("Tu compra ha finalizado, aqui tienes tu ticket: ")
    print (datetime.today())
    print (f'Te has ahorrado :{ahorro}')
    print (f'El importe final de la compra es: {importe}')
    
tienda_discos ()