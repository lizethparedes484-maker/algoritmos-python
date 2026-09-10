#“La langosta ahumada” es una empresa dedicada a ofrecer banquetes; sus tarifas son las siguientes: el costo de platillo por persona es de $95.00, pero si el número de personas es mayor a 200 pero menor o igual a 300, el costo es de $85.00. Para más de 300 personas el costo por platillo es de $75.00. Se requiere un algoritmo que ayude a determinar el presupuesto que se debe presentar a los clientes que deseen realizar un evento.

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
