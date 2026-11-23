#problema 10/20
"""
Evaluación de grupo académico (Aprobados, Reprobados y Excelencia): Lee las calificaciones finales de N estudiantes de un curso. Clasifícalos en tres categorías:
Reprobados (< 6. 0), Aprobados (6. 0 a 8. 9) y Excelencia (9. 0 a 10. 0). Muestra la cantidad de alumnos por categoría y el promedio general del grupo.
"""
#se inician los contadores y acumuladores en cero
reprobados = aprobados = excelencia = promedio = 0

#se pide la cantidad de calificaciones a evaluar mediante un input
Num = int(input("¿Cuantas calificaciones seran?: "))

#ciclo que empieza desde el 1 hasta la cantidad de veces ingresado mas 1
for i in range (1,Num+1):
    #pregunta la calificacion final de cada una
    categoria = float(input(f"¿Cual es la calificacion final {i}?: "))  
    #inician los condicionales para clasificar cada calificaion 
    if categoria < 6:
        #si la calificacion es menor a 6 el contador reprobados suma 1
        reprobados += 1
         
    elif categoria >=6 and categoria <= 8.9:
        #si la calificacion es mayor a 6 pero menor a 9 el contador aprobados suma 1
        aprobados += 1
         
    else:
        #si ningguna de las anteriores se cumple el contador excelencia suma 1
        excelencia += 1
    promedio += categoria
#calculo del promedio general
promedio2 = promedio / Num

#se imprimen los resultados 
print (f"La cantidad de alumnos en la categoria de reprobados son: {reprobados}")
print (f"La cantidad de alumnos en la categoria de aprobados son: {aprobados}")
print (f"La cantidad de alumnos en la categoria de excelencia son: {excelencia}")
print(f"El promedio general del grupo es {promedio2}")
