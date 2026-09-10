#IDiseña una función llamada mayor_de_tres(a, b, c) que reciba tres números y determine cuál es el mayor utilizando únicamente operadores lógicos (and) y comparaciones (>=), sin emplear max(). Por ejemplo: si a >= b y a >= c, el mayor es a. La función debe devolver el número más grande encontrado. Prueba 1: mayor_de_tres(5, 12, 9) Prueba 2: mayor_de_tres(20, 3, 1) Prueba 3: mayor_de_tres(4, 4, 4)

def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(mayor_de_tres(5, 12, 9))  
print(mayor_de_tres(20, 3, 1))  
print(mayor_de_tres(4, 4, 4))   