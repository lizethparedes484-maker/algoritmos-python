#problema 4/20

total = 0

for i in range(1,13):
    deposito = float(input("¿De cuanto es el deposito?:"))

    total += deposito
    print(f"El ahorro acumulado es : {total}")
t = 12000 - total
o = total - 12000
if total >= 12000:
    print(f"Logro superar la meta de ahorro($12000) por {o}")
else:
    print (f"Le falto {t} pesos para llegar a la meta")
print("El salario al cabo del total de años es $",total)
