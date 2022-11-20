#Utilizando la funcion area anterior, hacer un programa que nos muestre el volumen de un cilindro cuando nos introducen la altura.
#from Retos.Faciles.Reto13 import area_circulo
import math
def volumen_cilindro ():
  #area_circulo ()
  altura = float (input("Introduce la longitud del cilindro (en cm): "))
  radio = float (input("Introduce el radio del circulo (en cm): "))
  volumen = radio**2*math.pi*altura
  
  print (f"El volumen del cilindro es: {volumen} cm3")

volumen_cilindro ()

#Al subir los retos por separado, he tenido que comentar la funcion area_circulo y su importacion para que no me de error. 
# Si estuvieran ambos en un unico .py, unicamente deberia de descomentar y llamariamos a la funcion area_circulo para calcular el volumen.
