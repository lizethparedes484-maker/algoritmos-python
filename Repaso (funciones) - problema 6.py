#Crea una función llamada mayor_de_dos(a, b) que devuelva el número más grande sin usar la función integrada max(). Si son iguales, retorna cualquiera de los dos. Prueba 1: mayor_de_dos(15, 27): 27 Prueba 2: mayor_de_dos(40, -10): 40 Prueba 3: mayor_de_dos(8, 8): 8
# Definimos una función llamada 'mayor_de_dos' que recibe dos números: 'a' y 'b
def mayor_de_dos  (a,b):
    # Evaluamos si el número 'a' es más grande que 'b'
    if a>b :
        # Si es verdad, devolvemos el valor de 'a'
        return a
       # Si no es mayor (es decir, 'b' es más grande o son iguales)
    else:
        # Devolvemos el valor de 'b'
        return b
#comparamos e imprimimos
print (mayor_de_dos(12,9))
print (mayor_de_dos(40, -10))
print (mayor_de_dos(8,8))
