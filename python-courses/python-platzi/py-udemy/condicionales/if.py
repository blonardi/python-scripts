#condicional if

# dato = int(input("ingrese un numero: "))

# if dato > 0: 
#     print("numero positivo")
# elif dato == 0:
#     print("numero es cero")
# else:
#     print("numero es negativo")

#EJERCICIO 3

# nombre1 = input("Ingrese el primer nombre: ")
# nombre2 = input("Ingrese el segundo nombre: ")

# #con nombre[-1] conseguimos la ultima letra de la variable/input

# if nombre1[0] == nombre2[0] or nombre1[-1] == nombre2[-1]:
#     print("si hay coincidencia")
# else: 
#     print("no hay coincidencia")

#EJERCICIO 4

saldo = 2000

print("1. Ingresar dinero")
print("2. Retiro dinero")
print("3. Mostrar dinero")
print("4. Salir")

seleccion = int(input("Elija una opcion: "))

if seleccion == 1:
    ingreso = float(input("Dinero a ingresar: "))
    saldo += ingreso
    print(f"Tu saldo es: {saldo}")
elif seleccion == 2:
    retiro = float(input("Dinero a retirar: "))
    if retiro > saldo:
        print("Saldo insuficiente")
    else:     
        saldo -= retiro
        print(f"Tu saldo es: {saldo}")
        
elif seleccion == 3:
    print(f"Tu saldo es: {saldo}")
elif seleccion == 4:
    print("Gracias por trabajar con nosotros, vuelva prontos.")
else:
    print("***/ERROR/***")    