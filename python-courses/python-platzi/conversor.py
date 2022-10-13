def conversor(sueldo_usuario, moneda_extranjera):
    sueldo_convertido = (sueldo_usuario / moneda_extranjera)
    sueldo_convertido = round(sueldo_convertido,2)
    sueldo_convertido = str(sueldo_convertido)
    moneda_extranjera = str(moneda_extranjera)

    return("Tu sueldo convertido es: $" + sueldo_convertido )


menu = """
BIENVENIDO AL CONVERSOR DE MONEDAS

/**Elige una moneda de cambio para tus pesos **/

1 - Dolar Oficial $150
2 - Dolar Blue    $300
3 - Euro          $137
4 - Libra Esterlina $161

Elige una opcion: """

opcion = input(menu)

dolar_oficial = 150
dolar_blue = 300
euro = 137
libra = 161

sueldo_usuario = int(input("Ingresa tu sueldo en pesos argentinos: $"))


if opcion == '1':
    respuesta = conversor(sueldo_usuario, dolar_oficial)
    print(respuesta)
elif opcion == "2":
    respuesta = conversor(sueldo_usuario, dolar_blue)
    print(respuesta)
elif opcion == "3":
    respuesta = conversor(sueldo_usuario, euro)
    print(respuesta)
elif opcion == "4":
    respuesta = conversor(sueldo_usuario, libra)
    print(respuesta)
else: print("El numero introducido no es correcto.")    


