"""
Larisa Carolina Alvarez Gonzalez 763374
"""



# Entradas
numero1 = int(input("Introduzca un número: "))
numero2 = int(input("Introduzca otro número: "))


# Proceso
numero = 0
multiplo = 0

if numero1 % numero2 == 0:
    multiplo = numero1
    numero = numero2
elif numero2 % numero1 == 0:
    multiplo = numero2
    numero = numero1


# Salidas
print("El número " + str(multiplo) + " es múltiplo del " + str(numero))



