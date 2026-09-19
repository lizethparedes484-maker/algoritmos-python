#Determina cuánto pagará finalmente una persona por un artículo equis, considerando que tiene un descuento de 20%, y debe pagar 15% de IVA (debe mostrar el precio con descuento y el precio final). Crea un menú para que el usuario elija entre 2 productos y el que elija, despliegua el nombre de producto, precio, precio con descuento y precio final.
# Pedimos el precio original del producto
articulo = float(input("ingrese el costo del producto:"))

# Sacamos el 20% de descuento multiplicando por 20 y dividiendo entre 100
precio_descuento = articulo*20 / 100 

# Le restamos el descuento al precio original
articulo2 = articulo - precio_descuento
print(f"el producto con el 20% de descuento es: {articulo2}")

# Calculamos el 15% de IVA sobre el precio que ya tiene el descuento
precio_iva= articulo2*15 /100

# Le sumamos el IVA al precio descontado para obtener el precio final
precio3 = articulo2 + precio_iva 
print(f"el precio con mas iva es: {precio3}")

#le pedimosal usuario que elija entre huevoo o leche
input("elija entre huevo o leche: ")
# Guardamos los textos con la información de los precios para huevoo o leche
huevo = ("huevoo costo con descuento $8 costo con descuento e iva 7.36")
leche = ("leche costo con descuento $80, con descuento e iva 73.6")
#evaluamos la condicion para imprimir el producto elegido
if huevo:
    print (huevo);
else:
    print (leche);
