personas = int(input("¿Cuántos personas son? "))
   
if personas > 200 and personas <=300:
    costo = 85
    total = personas* costo
elif personas>= 300:
    costo = 70
    total = personas  * costo
else:
    costo = 95
    total = personas * costo
   
print("Costo por personas: $", costo)
print("total a pagra a la compañia :", total)