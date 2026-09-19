#Escribe una función llamada es_mayor_de_edad(edad) que reciba un entero y retorne "Mayor" si tiene 18 años o más, y "Menor" en caso contrario. Prueba 1: es_mayor_de_edad(17): "Menor" Prueba 2: es_mayor_de_edad(18): "Mayor" Prueba 3: es_mayor_de_edad(45): "Mayor"
# Definimos una función llamada 'es_mayor_edad' que recibe un valor llamado 'edad'
def es_mayor_edad (edad):
    # Evaluamos si la edad es 18 o más
    if edad >= 18:
        # Si cumple la condición, devolvemos el texto "mayor"
        return "mayor"
    # Si no, evaluamos si la edad está en el rango válido (menor a 18 y positiva)
    elif edad < 18 and edad >0:
        # Si se cumple las dos cosas, devolvemos "menor"
        return "menor"
    # Si la edad es 0 o un número negativo
    else:
        # Devolvemos un mensaje avisando que el número no es válido
        return " numero no valido"

print(es_mayor_edad(12))
print(es_mayor_edad(18))
print(es_mayor_edad(45))

        
        
