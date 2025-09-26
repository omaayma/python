importe = float(input("Introduce el importe a pagar en euros"))
meses = int(input("Introduce el número de meses"))
pagoMes = round(importe/meses, 2)
print("Tienes que pagar", pagoMes, "euros cada mes ")

