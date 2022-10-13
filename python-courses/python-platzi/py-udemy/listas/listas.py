#intro a listas

array = ["futbol","pc",18.6,18,[6,7,10.4],True,False,"pc"]
# print(len(array))
array.append(66)
# print(array)
# insertar en posicion 1, el num 88
array.insert(1,88)
# print(array)
array2 = [9,12,18]
array3 = array + array2
# print(array3)
array.remove("futbol")
#limpia array completo
array3.clear()
#da vuelta el array entero
array3.reverse()
#ordenar array asc // con reverse es desc
array.sort(reverse=True)
# print("pc" in array, muestra el indice)
print(array.index("pc"))
#contar la cantidad de "pc" que hay
print(array.count("pc"))