#Determina el promedio que obtendrá un alumno considerando que realiza tres exámenes, de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que el tercero de 50%

cal1 = float(input("ingrese la primera calificacion:"))
cal2 = float(input("ingrese la tercera calificacion:"))
cal3 = float(input("ingrese la tercera  calificacion:"))

cal11 = cal1*0.25
cal12= cal2 *0.25
cal13 = cal3 * 50

total = (cal1+cal2+cal3 ) / 3
print (f"el promedio es {total}")
