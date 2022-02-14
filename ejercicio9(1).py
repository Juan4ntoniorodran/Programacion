base = int(input("Introduzca el valor de la base "))
exponente = int(input("Introduzca el valor del exponente "))
if exponente>=1:
    potencia = base**exponente
    print (potencia)
if exponente==0:
    potencia = 1
    print (potencia)
if exponente<=-1:
    potencia= 1/(base**exponente)
    print (potencia)