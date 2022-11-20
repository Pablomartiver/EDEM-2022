#Programa que calcule la el area de un triangulo, recibiendo por consola la altura y la base. Luego hacer otra funcion que calcule el area de un circulo recibiendo el radio. Para no introducir el numero pi manualmente, utilizamos la funcion math.pi de la biblioteca

def area_triangulo ():
  base = float (input("Introduce la base del triangulo (en cm): "))
  altura = float (input("Introduce la altura del triangulo (en cm): "))
  area1 = float (base*altura/2)
  print (f"El area del triangulo es: {area1} cm2")

import math
def area_circulo ():
  radio = float (input("Introduce el radio del circulo (en cm): "))
  area2 = float (radio** 2 *math.pi)
  print (f"El area del circulo es: {area2} cm2")
