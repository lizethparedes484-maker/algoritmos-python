#problema 11/20
niños = adolescentes = adultos = adultosmayores = 0

Num = int(input("¿A cuantas personas se le realizara la encuesta?: "))
for i in range (1,Num +1):
    categoria = int(input(f"¿Cual es la edad del participante {i} ?: "))
    if categoria <= 12:
        niños += 1
       
    elif categoria >=13 and categoria <= 17:
        adolescentes += 1
        
    elif categoria >=18 and categoria <= 59:
        adultos += 1
       
    else:
        adultosmayores += 1
       
print (f"La cantidad de niños que participaron en la encuesta son: {niños}")
print (f"La cantidad de adolescentes que participaron en la encuesta son: {adolescentes}")
print (f"La cantidad de adultos que participaron en la encuesta son: {adultos}")
print (f"La cantidad de adultos mayores que participaron en la encuesta son: {adultosmayores}")
