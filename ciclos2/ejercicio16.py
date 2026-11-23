#problema 16/20
"""
Validación e intentos de cobro en cajero: Un usuario intenta retirar dinero de un cajero que solo permite hasta 3 intentos fallidos por saldo insuficiente o clave incorrecta. 
Si el usuario ingresa un monto mayor a su saldo disponible (N), descuenta un intento. El ciclo termina si el retiro es exitoso o si agota sus 3 intentos.
"""

# pregunta el saldo disponible y el NIP de referencia para realizar la operación
saldo_disponible = float(input("Ingresa tu saldo disponible: "))
nip = input("Ingresa tu NIP: ")

# inicialización del contador de intentos fallidos y de la bandera de estado (0 = no retirado, 1 = retiro exitoso)
intentos_fallidos = exito = 0

# ciclo  que otorga hasta 3 intentos para realizar el retiro
for i in range(1, 4):
    # solicitud de la clave ingresada en el intento actual y del monto que el usuario quiere retirar
    clave = input(f"Intento {i}, ingresa tu clave: ")
    monto = float(input("Ingresa el monto que desea retirar: "))

    # condicionales para validar la clave y el saldo disponible 
    if clave != nip:
        # contador que incrementa en 1 los intentos fallidos si la clave no coincide con el NIP
        intentos_fallidos += 1
        print(f"nip incorrecto,  Intentos fallidos: {intentos_fallidos}/3")
    elif monto > saldo_disponible:
        # contador que incrementa en 1 los intentos fallidos si el monto excede el saldo disponible
        intentos_fallidos += 1
        print(f"Saldo no suficiente,  Intentos fallidos: {intentos_fallidos}/3")
    else:
        # actualización del saldo restando el monto retirado
        saldo_disponible = saldo_disponible - monto
        # bandera de control: marca el retiro como exitoso (1)
        exito = 1
        print(f"\nRetiro exitoso. Entregando ${monto}")
        print(f"Saldo restante: ${saldo_disponible}")
        # inaliza el ciclo con un break
        break

    # condicional de seguridad que detiene el ciclo si se alcanzan los 3 intentos fallidos
    if intentos_fallidos == 3:
        break

# condicional final que informa si la operación no pudo completarse tras el ciclo
if exito == 0:
    print("Operación fallida")
