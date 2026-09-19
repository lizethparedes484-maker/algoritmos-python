#Escribe una función llamada longitud_nombre(nombre) que reciba una cadena y retorne cuántas letras tiene usando len(). Prueba 1: longitud_nombre("Lucía"): 5 Prueba 2: longitud_nombre("Sol"): 3 Prueba 3: longitud_nombre(""): 0
# Definimos una función llamada 'longitud_nombre' que recibe una palabra o texto en la variable 'nombre'
def longitud_nombre(nombre):
    # La función 'len()' cuenta cuántos caracteres tiene el texto y devuelve esa cantidad
    return len(nombre)

# Llamamos a la función con el nombre  e imprimimos el resultado 
print(longitud_nombre("Lucía"))  
print(longitud_nombre("Sol"))    
print(longitud_nombre(""))       



  

    
