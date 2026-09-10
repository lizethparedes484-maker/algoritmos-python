#Diseña una función llamada area_triangulo(base, altura) que calcule el área mediante la fórmula (base x altura) / 2 y valide que ambos valores sean mayores a cero; si no lo son, debe retornar 0. Prueba 1: area_triangulo(10, 5): 25.0 Prueba 2: area_triangulo(7, 4): 14.0 Prueba 3: area_triangulo(-2, 5): 0
def area_triangulo (base, altura):
    
    if base > 0 and altura > 0:
        return  (base*altura)/2 
    else: 
        return  "valores no validos"
   
    
print(area_triangulo(10, 5))
    

