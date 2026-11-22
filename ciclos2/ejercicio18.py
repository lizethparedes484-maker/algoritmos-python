#problema 18/20

dentro = infraccion = multagrave = 0

for i in range (1,13):
    vehiculo = float(input(f"¿A que velocidad iba el vehiculo {i}?"))
    if vehiculo <= 90:
        dentro += 1
    
    elif vehiculo > 110:
        multagrave += 1
        infraccion += 1
    else:
        infraccion += 1
print(f"La cantidad de vehiculos que iban dentro del limite son {dentro}")
print(f"La cantidad de vehiculos que superaron el limite son: {infraccion} y {multagrave} de ellos tienen multa grave por superar los 110 km/h")
    
