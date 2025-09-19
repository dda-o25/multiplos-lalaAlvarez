"""
Larisa Carolina Alvarez Gonzalez 763374
"""



# Entradas
numero1 = int(input("Introduzca un número: "))
numero2 = int(input("Introduzca otro número: "))


# Proceso
numero = 0
multiplo = 0
salida = ""
if numero1 == 0 and numero2 == 0:
    salida="Ninguno de los números es múltiplo del otro"    
else:
    if numero1 % numero2 == 0:
        multiplo = numero1
        numero = numero2
        salida = "El número " + str(multiplo) + " es múltiplo del " + str(numero)
    elif numero2 % numero1 == 0:
        multiplo = numero2
        numero = numero1
        salida = "El número " + str(multiplo) + " es múltiplo del " + str(numero)
    else:
        salida="Ninguno de los numeros es múltiplo del otro"    


# Salidas
print(salida)



