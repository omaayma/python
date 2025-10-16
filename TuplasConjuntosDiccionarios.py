"""
tupla =(1,2,3,4,5)
print(tupla)
tupla2 = ("Juanjo", "Lucía")
tupla3 = (1,2,"Hola")
print(tupla2)
print(tupla3)
tupla4=("Sevilla",)
print(tupla4)

for elemento in tupla4:
    print(elemento)

for i in range(0, len(tupla4)):
    print(i, "-", tupla4[i])

Lista = list(tupla2)
print(Lista)

texto = str(tupla2)
print(texto)

tupla5= tuple(1,2,3,4,5)
print(tupla5)
tupla6 = tuple("Hola mundo")
print(tupla6)

tupla7 = "Pepe", tupla3,"Juan"
print(tupla7)

if 8 not in tupla:
    print("El 8 no está en la tupla")

profesor = ("José María", "Morales", 57, False, True)
nombre, apellidos,edad,alumno, profe = profesor
print(apellidos, edad)



#CONJUNTOS
profesPrimero = ("Pepe","Lucía","David")
print(profesPrimero)  #tambien sepuede hacer con set
if "José María" in profesPrimero:
    print("José María está en primero")
if "José María" not in profesPrimero:
    print("José María no esta")

for elemento in profesPrimero:
    print(elemento)

profesPrimero.add("Raqauel")
print(profesPrimero)

profesPrimero.remove("Lucía")
profe = profesPrimero.pop()
print(profe)
print(profesPrimero)
profesPrimero.clear()
print(profesPrimero)
"""
conjunto1 = set([1,2,3,4,5])
print(conjunto1)
conjunto2 = set ("Hola mundo")
print(conjunto2)
profesPrimero = ("JUan", "Lucía", "Rauqel")
profesSegundo = ("JUan", "David")

#Conversiones
print(profesPrimero | profesSegundo) #union, muestran los elementos de uno y otro sin duplicados
print(profesPrimero & profesSegundo) #interseccion, muestran los elementos que tienene en comun los dos
print(profesPrimero - profesSegundo) #diferencia, aparecen los elementos de uno u oto sin los comunes, el orden afecta al resultadp
print(profesSegundo-profesPrimero)
#print(profesPrimero )

print(profesPrimero.union(profesSegundo))
print(profesPrimero.intersection(profesSegundo))
print(profesPrimero)

