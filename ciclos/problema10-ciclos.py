#problema 10 ciclos
#Una discoteca tiene 8 personas registradas. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).
contador = 0 #el contador inicia en cero
edades  = [12, 23,45,67,78,89,23,23] #las edades a evaluar son las que estan dentro de la lista
for i in range(8): #como son 8 valores se va a repetir 8 veces
    
    if(edades[i] < 18): #si alguna edad dentro de la lista es menor a 18
        print(f"no puedes pasar{edades[i]}") #se imprime "no puedes pasar"
        contador += 1   #ademas contador suma uno
print("las personas que no pueden pasar son ", contador) #se imprime el resultado final
