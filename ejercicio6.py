x1= int(input("Introduzca el primer valor de x "))
x2= int(input("Introduzca el segundo valor de x "))
y1= int(input("Introduzca el primer valor de y "))
y2= int(input("Introduzca el segundo valor de y "))
import math
distancia= math.sqrt((x2-x1)**2+(y2-y1)**2)
print ("La distancia entre el primer punto y el segundo punto es: "+ str(distancia))