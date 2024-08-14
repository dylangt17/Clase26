def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

# Ejemplo de uso
total_cuenta = float(input("Ingresa el total de la cuenta: "))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))

propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)
print(f"Debes dejar una propina de: ${propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")


def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_pagar = total_cuenta + propina
    return propina, total_pagar

# Ejemplo de uso
total_cuenta = float(input("Ingresa el total de la cuenta: "))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))

propina, total_pagar = calcular_propina(total_cuenta, porcentaje_propina)

print(f"Debes dejar una propina de: ${propina:.2f}")
print(f"El total a pagar es: ${total_pagar:.2f}")

# Agregar la opción de dividir la cuenta entre varias personas
numero_personas = int(input("¿Cuántas personas compartirán la cuenta? "))

if numero_personas > 0:
    total_por_persona = total_pagar / numero_personas
    print(f"Cada persona debe pagar: ${total_por_persona:.2f}")
else:
    print("El número de personas debe ser mayor que 0.")
