#Crea una función llamada obtener_signo(numero) que reciba un número real o entero. Mediante las ramas if, elif y else, clasifica el valor: retorna "Positivo" si es mayor que cero, "Negativo" si es menor que cero, o "Cero" si es exactamente igual a cero. Prueba 1: obtener_signo(12): "Positivo" Prueba 2: obtener_signo(-8): "Negativo" Prueba 3: obtener_signo(0): "Cero"
# Definimos una función llamada 'obtener_signo' que recibe un 'numero'
def obtener_signo  (numero):
    # Evaluamos si el número es mayor a 1 para positivo
    if numero > 1 :
        return "positivo"
    # Si es menor a 1, asumimos que es negativo
    elif numero < 1 :
        return "negativo"
    # Si no es mayor ni menor a 1, devolvemos "cero"
    else:
        return "cero"

# Evaluamos e imprimimos
print (obtener_signo(12))
print (obtener_signo(-8))
print (obtener_signo(0))
