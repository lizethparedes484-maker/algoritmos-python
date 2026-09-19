#Se requiere determinar cuál de tres cantidades proporcionadas es la mayor.
# Pedimos al usuario que ingrese tres números
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

# Evaluamos cuál de los tres números es el mayor:
if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num3

# Imprimimos el resultado
print(f"\nLa cantidad mayor es: {mayor}")
