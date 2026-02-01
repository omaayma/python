from rope.base.builtins import Lambda


def cuadrado(r):
    return r**2

print(cuadrado(2))
cuadradoLambda = lambda r: r**2
print((cuadradoLambda(5)))


#usar lambda para un ejercicio de hacer media para una lista de números

cuadradoMayorPieza = lambda r: True if r**2>=10 else False
print(cuadradoMayorPieza(4))
print(cuadradoMayorPieza(1))