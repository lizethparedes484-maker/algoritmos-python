#Implementa una función llamada operacion_basica(a, b, operacion) donde a y b son operandos numéricos y operacion es una cadena. Usa ramas condicionales para comparar el texto: si vale "suma", devuelve a + b; si vale "resta", devuelve a - b; si vale "multiplica", devuelve a x b. Si el texto recibido no coincide con ninguna de esas opciones, debe retornar "Operación no válida" Prueba 1: operacion_basica(6, 4, "resta"): 2 Prueba 2: operacion_basica(5, 3, "multiplica"): 15 Prueba 3: obtener_signo(0): operacion_basica(10, 2, "raiz"): "Operación no válida"
# Definimos la función 'operacion_basica' que recibe dos números ('a' y 'b') y un texto con el tipo de 'operacion'
def operacion_basica(a, b, operacion):
    # Verificamos si la operación solicitada es "suma"
    if operacion == "suma":
        # Si coincide, sumamos
        return a + b
    # Si no es suma, revisamos si es "resta"
    elif operacion == "resta":
        # Si es así, restamos
        return a - b
    # Si no, comprobamos si es "multiplica"
    elif operacion == "multiplica":
        # De ser así, multiplicamos
        return a * b
    # Si escribió cualquier otra cosa que no esté entre las opciones anteriores
    else:
        # Mostramos un mensaje que esa operación no es valida
        return "Operación no válida"

#ejecutamos e imprimimos
print(operacion_basica(6, 4, "resta"))       
print(operacion_basica(5, 3, "multiplica")) 
print(operacion_basica(10, 2, "raiz"))      
