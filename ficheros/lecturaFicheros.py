
"""
    #r-lectura      #t-texto
    #w-escritura    #b-binario
    #a-append       #+-modo lectura y escritura combinado con otras letras


    #texto=fichero.read()
    #print(texto)
    #tengo que comentar esto por que si no no funciona lo de después, ya que el cursor ya está al final del fichero

    lineas=fichero.readlines()
    # print(lineas)

    for l in lineas:
        if(l[-1]=="\n"):
            print(l[:-1])  # para que se imprima suprimiendo el \n, el ultimo caracter de la linea

    #otra manera
    for i in range(len(lineas)):
        lineas[i]=lineas[i].replace('\n','')
        print(lineas[i]) """
try:
    # si solo ponemos un parametro, abrimos el fichero en modo lectura y escritura || si no ponemos r o t
    fichero = open('quijote.txt')
    #linea=fichero.readline()
    linea=fichero.readline(5)

    while linea !="":
        print(linea)
        #linea=fichero.readline()
        linea=fichero.readline(5)



    fichero.close()
except:
    print("Error, el fichero no existe")

#read-lee fichero completo y lo almacenamos en una variable de texto
#readLine- lee un a linea, si le ponemos readLine(2) solo lee 2 caracterees
#readLines- lee fichero entero y lo almacena en una lista, cada linea es un elemento de la lista
