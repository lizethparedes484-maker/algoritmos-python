#problema 16/20
saldo_disponible = float(input("Ingresa tu saldo disponible: "))
nip = input("Ingresa tu NIP: ")

intentos_fallidos = exito =0
  # 0 = no retirado, 1 = retiro exitoso

for i in range(1, 4):
    clave = input(f"Intento {i}, ingresa tu clave: ")
    monto = float(input("Ingresa el monto que desea retirar: "))

    if clave != nip:
        intentos_fallidos += 1
        print(f"nip incorrecto,  Intentos fallidos: {intentos_fallidos}/3")
    elif monto > saldo_disponible:
        intentos_fallidos += 1
        print(f"Saldo no suficiente,  Intentos fallidos: {intentos_fallidos}/3")

    else:
        saldo_disponible = saldo_disponible - monto
        exito = 1
        print(f"\nRetiro exitoso. Entregando ${monto}")
        print(f"Saldo restante: ${saldo_disponible}")
        break

    if intentos_fallidos == 3:
        break

if exito == 0:
    print("Operación fallida")
