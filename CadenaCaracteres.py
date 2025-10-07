"""
lista1 = []
lista2 = list()
lista3 = [2, 4, 67,5, 8,4,8,9]
lista4 = ["Juanjo", "Pepe", "Ana"]
print(lista3)
texto = str(lista3) #cadena de texto igual que la lista
print(texto)
texto2= "Hola mundo"
lista5 = list(texto) #para convertir el texto a lista
print(lista5)


lista5 = list(texto2)
print(lista5)
matriz ={[1,2,3], [4,5,6]}
print(matriz[1][0])



#lista5 = lista3 + lista4 #concatenar
#lista3.extend(lista4) #concatenar
#lista2.append(14) #metele elemento al final de lista
lista3.insert(2,15) #inserta el 15 antes del 2
print(lista3)
print(lista3.count(4)) #para contar cuantas vveces aparece el 4
print(lista3.index(5))  #para la posición donde está el 5
"""

import random
lista = ["Pepe", "JUan", "Lucía", "Nicolás"]
print(random.choice(lista))
print(random.sample(lista, 3))
print(random.shuffle(lista))
print(lista)


#isDigit, Isnum, Isalpha, IsSpace,isDecimal