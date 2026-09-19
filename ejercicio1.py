#Una empresa importadora desea determinar cuántos dólares puede adquirir con equis cantidad de dinero mexicano.
# Guardamos en una variable a cuántos pesos equivale un dólar
dolar = 16.96

#le pedimos al usuario que ingrese la cantidad en pesos y la convertimos en numeros decimales con el float
pesos = float(input("ingrese los pesos mexicanos a convertir"))

# Calculamos la conversion dividiendo los pesos entre el valor del dólar
conversion = pesos / dolar

#mostramos el resultado
print(f"su monto equivale a {conversion}, dolares")
