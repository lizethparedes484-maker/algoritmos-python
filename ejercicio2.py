#Una empresa que contrata personal requiere determinar la edad de las personas que solicitan trabajo, pero cuando se les realiza la entrevista sólo se les pregunta el año enque nacieron.
# Le pedimos al usuario su año de nacimiento y lo pasamos a un número entero
persona_edad = int(input("ingrese su año de nacimiento"))

#definimos el año como punto de referencia
año_actual= 2026

# Restamos el año de nacimiento al año actual para calcular los años cumplidos
edad = año_actual - persona_edad

#mostramos el resultado
print (f"su edad es {edad}")
