datoa= int(input("Introduzca el valor de A "))
datob= int(input("Introduzca el valor de B "))
datoc= int(input("Introduzca el valor de C "))
import math
pitagoras=math.sqrt(datoa**2+datob**2)
if datoc==pitagoras:
    print ("El triangulo es rectangulo")
if datoa==datob:
    print("El triangulo es isosceles")
if datoa==datob or datoa==datoc:
    print("El triangulo es equilatero")
