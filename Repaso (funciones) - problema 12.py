#Problema: Crea una función llamada calificar(nota) que reciba un número decimal o entero que represente una calificación de 0 a 100. Utilizando una cadena de condiciones if / elif / else: Si la nota es mayor o igual a 90, retorna "A" Si está entre 80 y 89 inclusive, retorna "B" .Si está entre 70 y 79 inclusive, retorna "C" Si es menor estrictamente a 70, retorna "F" .
# Definimos la función 'calificar' que recibe un valor numérico en la variable 'nota'
def calificar(nota):
    # revisamos si nota es de 90 o superior para la calificación máxima
    if nota >= 90:
        # Si llega a 90 o más, ponemos la letra "A"
        return "A"
    # Si fue menor a 90, revisamos si llega  a 80
    elif nota >= 80:
        # En el rango de 80 a 89, asignamos la letra "B"
        return "B"
    # Si fue menor a 80, comprobamos si alcanza el 70    
    elif nota >= 70:
        # En el rango de 70 a 79, asignamos la letra "C"
        return "C"
   # Si la nota es menor a 70 
    else:
        # Para cualquier calificación por debajo de 70, ponemos la letra "F"
        return "F"

#evaluamos e imprimimos
print(calificar(95))  
print(calificar(85))  
print(calificar(72))  
print(calificar(65))  
