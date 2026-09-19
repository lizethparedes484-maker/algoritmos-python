#Diseña una función llamada mayor_de_tres(a, b, c) que reciba tres números y determine cuál es el mayor utilizando únicamente operadores lógicos (and) y comparaciones (>=), sin emplear max(). Por ejemplo: si a >= b y a >= c, el mayor es a. La función debe devolver el número más grande encontrado. Prueba 1: mayor_de_tres(5, 12, 9) Prueba 2: mayor_de_tres(20, 3, 1) Prueba 3: mayor_de_tres(4, 4, 4)
# Definimos la función 'mayor_de_tres' que recibe tres números: 'a', 'b' y 'c'
def mayor_de_tres(a, b, c):
    # Evaluamos si 'a' es mayor o igual que 'b' como a 'c'
    if a >= b and a >= c:
        # Si 'a' es mayor, nos quedamos con 'a'
        return a
    # Si no, pero 'b' es mayor o igual a 'a' y a 'c'
    elif b >= a and b >= c:
        # Entonces el número más grande es 'b'
        return b
    # Si ni 'a' ni 'b' son los mayores, por lógica el mayor es 'c'
    else:
        return c

#comparamos e imprimimos
print(mayor_de_tres(5, 12, 9))  
print(mayor_de_tres(20, 3, 1))  
print(mayor_de_tres(4, 4, 4))   
