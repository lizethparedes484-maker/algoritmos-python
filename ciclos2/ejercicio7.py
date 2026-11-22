# problema 7/20
media = 0

mayor = 0
menor = 0
for i in range (1,31,1):
    temperatura = float(input(f"cual es la temperatura en el dia {i} "))
    if i == 1:
        menor = temperatura
        mayor = temperatura
    if temperatura < menor:
        menor = temperatura
        
    if temperatura > mayor:
        mayor = temperatura
    media += temperatura
       
  
    
tempm= media/30

print (f"la temperatura mas alta registrada es: {mayor}")
print (f"la temperatura mas baja registrada es: { menor}")
print (f"la temperatura media del mes es: {tempm} ")
