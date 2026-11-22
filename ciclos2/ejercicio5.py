# problema 5/20
electronica1 = ropa2 = alimentos3 = 0


articulos = int(input("¿Cuantos son el numero de articulos?: "))
print ("Categorias: 1Electronica, 2Ropa, 3Alimentos")
for i in range ( articulos):
    clasificacion = int(input("A que categoria pertenece 1, 2 o 3: "))
    if clasificacion == 1:
        electronica1 += 1
    elif clasificacion == 2: 
        ropa2 += 1
    elif clasificacion==3: 
        alimentos3 += 1
porcentajelec = (electronica1/articulos)*100
porcentajerop = (ropa2/articulos)*100
porcentajealim = (alimentos3/articulos)*100

print (f"La cantidad de articulos que hay en electronica: {electronica1}, y el porcentaje es: {porcentajelec}% ")
print (f"La cantidad de articulos que hay en ropa: {ropa2}, y el porcentaje es: {porcentajerop} %")
print (f"La cantidad de articulos que hay en alimentos: {alimentos3}, y el porcentaje es: {porcentajealim}% ")
