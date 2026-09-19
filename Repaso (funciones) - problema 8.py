#Diseña una función llamada area_triangulo(base, altura) que calcule el área mediante la fórmula (base x altura) / 2 y valide que ambos valores sean mayores a cero; si no lo son, debe retornar 0. Prueba 1: area_triangulo(10, 5): 25.0 Prueba 2: area_triangulo(7, 4): 14.0 Prueba 3: area_triangulo(-2, 5): 0
# Definimos una función llamada 'area_triangulo' que recibe la 'base' y la 'altura'
def area_triangulo (base, altura):
    # Comprobamos que tanto la base como la altura sean números positivos 
    if base > 0 and altura > 0:

        # Si son válidas, aplicamos la fórmula del área (base * altura / 2) y devolvemos el resultado
        return  (base*altura)/2 
    # Si alguno de los valores es 0 o negativo
    else: 
        # Devolvemos un mensaje diciendo que los valores no son válidos
        return  "valores no validos"
   
# Calculamos el área de un triángulo con base  y altura e imprimimos el resultado
print(area_triangulo(10, 5))
print(area_triangulo(7, 4))
print(area_triangulo(-2, 5))
    

