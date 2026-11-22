#problema 3/20
capital = 2000
total = 0
N = int(input("¿Cuantos son los años?: "))
for i in range(N):
    capital += capital*0.08
    total += capital
    print(f"El sueldo ganado en el año {i + 1} es: {capital}")
print("El salario al cabo del total de años es", total)
