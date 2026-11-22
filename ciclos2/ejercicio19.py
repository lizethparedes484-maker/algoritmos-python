#problema 19/20
capacidad_total = 1000
limite = capacidad_total*0.95
suma = suma2 = 0
for i in range (1, 1000 + 1):
    volumendescarga = float(input(f"Ingrese los litros de la descarga {i}:"))
    suma2 += 1 
    suma += volumendescarga
    if suma >= limite :
        print(f"El tanque ha llegado a su limite")
        break
print(f"Se necesitaron {suma2} descargas para llegar al limite del tanque")
print(f"El volumen total almacenado es de {suma} litros")
