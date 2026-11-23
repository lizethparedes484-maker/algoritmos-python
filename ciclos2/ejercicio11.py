#problema 11/20
"""
Estadística de edades por rangos: En una encuesta aplicada a N personas, se registra la edad de cada participante. Clasifica y cuenta cuántas personas son niños
(0-12 años), adolescentes (13-17 años), adultos (18-59 años) y adultos mayores (60 años o más).
"""
#se inician todos los contadores en cero
niños = adolescentes = adultos = adultosmayores = 0

#pregunta la cantidad de personas que realizaron la encuesta
Num = int(input("¿A cuantas personas se le realizara la encuesta?: "))
#ciclo que comienza en uno y termima en la cantidad de veces ingresadas mas 1 (esto se hace hace para compensar que se inicio en uno)
for i in range (1,Num +1):
    categoria = int(input(f"¿Cual es la edad del participante {i} ?: ")) #pregunta la edad de cada paricipante mediante un input

    #inicin los condicionales para clasificar las edades 
    if categoria <= 12:
        #si la edad ingresada es menor o igual a 12 el contador niños suma 1
        niños += 1
    elif categoria >=13 and categoria <= 17:
        #si la edad ingresada es mayor o igual a 13 el contador adolescentes suma 1
        adolescentes += 1
        
    elif categoria >=18 and categoria <= 59:
        #si la edad ingresada es mayor o igual a 18 pero menor a 60 el contador adultos suma 1
        adultos += 1
       
    else:
        #si ninguna de las  anteriores se cumple el contador de adultos mayores suma 1
        adultosmayores += 1
#se imprimen todos los resultados     
print (f"La cantidad de niños que participaron en la encuesta son: {niños}")
print (f"La cantidad de adolescentes que participaron en la encuesta son: {adolescentes}")
print (f"La cantidad de adultos que participaron en la encuesta son: {adultos}")
print (f"La cantidad de adultos mayores que participaron en la encuesta son: {adultosmayores}")
