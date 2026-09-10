#Problema: Crea una función llamada calificar(nota) que reciba un número decimal o entero que represente una calificación de 0 a 100. Utilizando una cadena de condiciones if / elif / else: Si la nota es mayor o igual a 90, retorna "A" Si está entre 80 y 89 inclusive, retorna "B" .Si está entre 70 y 79 inclusive, retorna "C" Si es menor estrictamente a 70, retorna "F" .
def calificar(nota):
    if nota >= 90:
        return "A"
    elif nota >= 80:
        return "B"
    elif nota >= 70:
        return "C"
    else:
        return "F"


print(calificar(95))  
print(calificar(85))  
print(calificar(72))  
print(calificar(65))  