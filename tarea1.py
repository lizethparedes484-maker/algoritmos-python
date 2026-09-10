#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús es de $4000.00, sin importar el número de alumnos.

alumnos = int(input("¿Cuántos alumnos van al viaje? "))
if alumnos >= 100:
    costo = 65
    total = alumnos * costo
elif alumnos >= 50:
    costo = 70
    total = alumnos * costo
elif alumnos >= 30:
    costo = 95
    total = alumnos * costo
else:
    total = 4000
    costo = total / alumnos
print(f"Costo por alumno: $", costo)
print(f"total a pagra a la compañia :$ ", total)
