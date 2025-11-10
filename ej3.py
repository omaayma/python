texto = input("Escribe un texto:")
vocales = "aeiouAEIOU"
espacio = " "

textoNuevo=str(texto)

textoNuevo= textoNuevo.replace("a", "")
textoNuevo= textoNuevo.replace("A", "")
textoNuevo=textoNuevo.replace("E", "")
textoNuevo=textoNuevo.replace("e", "")
textoNuevo= textoNuevo.replace("I", "")
textoNuevo=textoNuevo.replace("i", "")
textoNuevo=textoNuevo.replace("O", "")
textoNuevo=textoNuevo.replace("o", "")
textoNuevo=textoNuevo.replace("U", "")
textoNuevo=textoNuevo.replace("u", "")
textoNuevo=textoNuevo.replace(" ", "")


print("Sin vocales ni espacios:", textoNuevo)
print("Vocales suprimidas:", vocales.count("aeiouAEIOU"))
print("Espacios en blanco suprimidos:", espacio.count(" "))
