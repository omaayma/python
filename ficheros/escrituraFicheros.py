# write- escribe texto que pasemos por argumento
# writeLines- escrib elas lineas que se pasen


try:
    fichero = open("quijote.txt","wt") #at

    #fichero.write("En un lugar de la Mancha\n")
    #fichero.write("de cuyo nombre no quiero acordarme\n")
    #fichero.write("\tno ha mucho que vivía\n")

    lista=["Jorge","Eva","Ana","Pepe"]
    fichero.writelines(lista)

    fichero.close()
except:
    print("Error")


try:
    with open("quijote.txt","wt") as fichero:
        fichero.write("Uno\n")  #no se pueden poner numeros directamente hay que ponerlo en modo texto
        fichero.write("Dos\n")
        fichero.write("Tres\n")
except:
    print("Error")