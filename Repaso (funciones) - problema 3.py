#Diseña una función llamada repetir_texto(texto, veces) que devuelva la palabra repetida la cantidad de veces indicada. Prueba 1: repetir_texto("Eco", 3): "EcoEcoEco"Prueba 2: repetir_texto("Hola", 1): "Hola" Prueba 3: repetir_texto("Ja", 4): "JaJaJaJa"
# Definimos la función que recibe un texto y el número de veces que quiero que se repita
def repetir_texto (texto, veces):
    # Multiplicamos el texto por 'veces' para duplicarlo ese número de ocasiones y lo devolvemos
    return texto*veces

print (repetir_texto("darinel ",4))
print (repetir_texto("hola",1))
print (repetir_texto("Ja ",4))




