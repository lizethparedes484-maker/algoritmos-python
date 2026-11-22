 #problema 1/20

#los contadores inician en  cero
hh= 0
ttotal = 0
sueldohora = 100   #declaramos un sueldo fija 

for i in range (6):    #se inicia los ciclos 
    horas= int(input(f"¿Cuantas son las horas trabajadas en el dia {i+1} ? "))   #se piden las horas trabajadas 
    
    # condicionales: si horas son menores o iguales a 8 el sueldo es normal y se va acumulando al total
    if (horas <= 8):
        sueldototal = horas*sueldohora  
        ttotal += sueldototal
    
    # si no cumple la primera condicion las horas extras se pagan al doble y se va acumulando al total
    elif(horas>8):
        horas2 = horas-8
        sueldototal= (horas2*(sueldohora*2)) + 800
        ttotal += sueldototal
        hh +=horas2
#se imprimen los resultados
print(f"El sueldo total semanal es ${ttotal} ")
print(f"El numero de horas extras trabajadas son {hh}")
