#problema 4/20
"""
Plan de ahorro mensual con meta variable: Una persona desea ahorrar dinero mes a mes durante un año. Al final de cada mes ingresa el monto depositado. El programa
debe mostrar el acumulado mes tras mes y, al finalizar los 12 meses, indicar si logró superar una meta fija de $12,000 y por cuánto la superó o cuánto le faltó.
"""
#inicia el acumulador 
total = 0

#se cumpliran doce ciclos (meses del año)
for i in range(1,13):
    deposito = float(input("¿De cuanto es el deposito?:")) #se pregunta la cantidad del deposito desde un input

    #ese deposito se acumula en el total
    total += deposito
    #se imprime esa cantidad acumulada
    print(f"El ahorro acumulado es : {total}")
t = 12000 - total  #la resta representa la cantidad que falta si no se alcanzo la meta
o = total - 12000  #esta resta representa la cantidad extra si se supero la meta 

#se evalua con los condicionales si se alcanzo o no la meta y se imprime 
if total >= 12000:
    print(f"Logro superar la meta de ahorro($12000) por {o}")
else:
    print (f"Le falto {t} pesos para llegar a la meta")
#se imprime el total
print("El salario al cabo del total de años es $",total)
