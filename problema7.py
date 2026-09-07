articulo = float(input("ingrese el costo del producto:"))
precio_descuento = articulo*20 / 100 
articulo2 = articulo - precio_descuento
print(f"el producto con el 20% de descuento es: {articulo2}")
precio_iva= articulo2*15 /100

precio3 = articulo2 + precio_iva 
print(f"el precio con mas iva es: {precio3}")

input("elija entre huevo o leche: ")
huevo = ("huevoo costo con descuento $8 costo con descuento e iva 7.36")
leche = ("leche costo con descuento $80, con descuento e iva 73.6")
if huevo:
    print (huevo);
else:
    print (leche);
