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
