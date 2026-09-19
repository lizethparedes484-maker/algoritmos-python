#Determina el promedio que obtendrá un alumno considerando que realiza tres exámenes, de los cuales el primero y el segundo tienen una ponderación de 25%, mientras que el tercero de 50%
#pedimos las tres calificaciones al usuario
cal1 = float(input("ingrese la primera calificacion:"))
cal2 = float(input("ingrese la segunda calificacion:"))
cal3 = float(input("ingrese la tercera  calificacion:"))

#calculamos el valor de cada calificacion segun su porcentaje (0.25, 0.25, 0.50)
cal11 = cal1*0.25
cal12= cal2 *0.25
cal13 = cal3 * 0.50

#sumamos los porcentajes obtenidos para sacar la calificacion final 
total = (cal11+cal12+cal13 ) 
#mostramos el resultado
print (f"el promedio es {total}")
