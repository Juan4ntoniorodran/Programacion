catetomayor = int(input("Introduzca las dimensiones del cateto mayor "))
catetomenor = int(input("Introduzca las dimensiones del cateto menor "))
import math
hipotenusa = math.sqrt(catetomayor**2+catetomenor**2)
print ("La hipotenusa es igual a "+ str(hipotenusa))