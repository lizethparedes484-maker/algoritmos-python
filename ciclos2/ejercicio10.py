#problema 10/20
reprobados = aprobados = excelencia = promedio = 0


Num = int(input("¿Cuantas calificaciones seran?: "))
for i in range (1,Num+1):
    categoria = int(input(f"¿Cual es la calificacion final {i}?: "))
    if categoria < 6:
        reprobados += 1
         
    elif categoria >=6 and categoria <= 8.9:
        aprobados += 1
         
    else:
        excelencia += 1
    promedio += categoria
promedio2 = promedio / Num

print (f"La cantidad de alumnos en la categoria de reprobados son: {reprobados}")
print (f"La cantidad de alumnos en la categoria de aprobados son: {aprobados}")
print (f"La cantidad de alumnos en la categoria de excelencia son: {excelencia}")
print(f"El promedio general del grupo es {promedio2}")
