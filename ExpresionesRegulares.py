

"""aqui damos siar(busca en toda), match(busca coincidencia al princii cadena), fullmatch() busca la misma coincidencia en tdo"""
"""
import re

patron = r"hola"
if re.match(patron, "hola"):
    print("Has coincidido")
else:
    print("No has coincidido")
   
   

import re

patron = r"hola"
texto = "hello"
if re.fullmatch(r"[0-9]{8][A-Z]", "12345678A"): #para el dni
    print("Has coincidido")
else:
    print("No hay coincidencia")

import re

patron = r"hola"
texto = "hello"
if re.fullmatch(r"[0-9]?", "6"): #EN EL CASO DE QJE APAREZCA ALGO ENTRE EL 0-9
    print("Has coincidido")
else:
    print("No hay coincidencia"
"""
import re

patron = r"hola"
texto = "hello"
if re.fullmatch(r"[^5]", "5"):  #CUALQUIER COSA QUE NO SEA EL 5
    print("Has coincidido")
else:
    print("No hay coincidencia")









