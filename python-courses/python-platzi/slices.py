# nombre = "francisco"
# nombre[0:4]

#PALINDROMOS




def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input("Ingrese una palabra para comprobar: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo tu palabra")
    else:
        print("No es palindromo")


if __name__ == '__main__':
    main()