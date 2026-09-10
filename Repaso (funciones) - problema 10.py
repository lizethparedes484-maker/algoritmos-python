#Implementa una función llamada operacion_basica(a, b, operacion) donde a y b son operandos numéricos y operacion es una cadena. Usa ramas condicionales para comparar el texto: si vale "suma", devuelve a + b; si vale "resta", devuelve a - b; si vale "multiplica", devuelve a x b. Si el texto recibido no coincide con ninguna de esas opciones, debe retornar "Operación no válida" Prueba 1: operacion_basica(6, 4, "resta"): 2 Prueba 2: operacion_basica(5, 3, "multiplica"): 15 Prueba 3: obtener_signo(0): operacion_basica(10, 2, "raiz"): "Operación no válida"

def operacion_basica(a, b, operacion):
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplica":
        return a * b
    else:
        return "Operación no válida"

print(operacion_basica(6, 4, "resta"))       
print(operacion_basica(5, 3, "multiplica")) 
print(operacion_basica(10, 2, "raiz"))      