# problema 5/20
"""
Inventario y conteo por tipo de producto: En una bodega hay un lote de N artículos clasificados por su tipo mediante un código (1: Electrónica, 2: Ropa, 3: Alimentos).
Cuenta cuántos artículos hay de cada tipo y calcula el porcentaje que representa cada categoría sobre el total.
"""
#inician los acumuladores en cero
electronica1 = ropa2 = alimentos3 = 0


articulos = int(input("¿Cuantos son el numero de articulos?: ")) #se  pregunta el numero de articulos mediante un input
print ("Categorias: 1Electronica, 2Ropa, 3Alimentos")            #se imprimen las categorias disponibles 

#se inicia el ciclo para evaluar los articulos 
for i in range ( articulos):                                     
    clasificacion = int(input("A que categoria pertenece 1, 2 o 3: ")) #se pregunta a que categoria pertenece el articulo mediante un input

    #inician los condicionales y contadores 
    if clasificacion == 1:
        #si el usuario ingreso 1 este contador suma 1
        electronica1 += 1
    elif clasificacion == 2: 
         #si el usuario ingreso 2 este contador suma 1
        ropa2 += 1
    elif clasificacion==3: 
         #si el usuario ingreso 1 este contador suma 1
        alimentos3 += 1
# se calcula el porcentaje de cada categoria 
porcentajelec = (electronica1/articulos)*100
porcentajerop = (ropa2/articulos)*100
porcentajealim = (alimentos3/articulos)*100

#se imprime cada resultado 
print (f"La cantidad de articulos que hay en electronica: {electronica1}, y el porcentaje es: {porcentajelec}% ")
print (f"La cantidad de articulos que hay en ropa: {ropa2}, y el porcentaje es: {porcentajerop} %")
print (f"La cantidad de articulos que hay en alimentos: {alimentos3}, y el porcentaje es: {porcentajealim}% ")
