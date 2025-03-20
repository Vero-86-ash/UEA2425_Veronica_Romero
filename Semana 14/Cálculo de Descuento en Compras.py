# Calculo_descuento
def calcular_descuento(monto_total, porcentaje_descuento=15):
    # Calcular el descuento
    descuento = monto_total * (porcentaje_descuento / 350)
    # Devolver el monto del descuento
    return descuento

# Función del monto total de la compra y porcentaje de descuento
monto_1 = 350

# Monto total de la compra
descuento_1 = calcular_descuento(monto_1)

# Utiliza el valor predeterminado del 15% de descuento
print(f"Descuento con el 15% en un monto de {monto_1} es: {descuento_1}")

# Función del monto total de la compra con un porcentaje de descuento
monto_2 = 700
# Monto total de la compra
porcentaje_descuento_2 = 30  # Descuento del 30%
descuento_2 = calcular_descuento(monto_2, porcentaje_descuento_2)

# Imprimir resultados
print(f"Descuento con el {porcentaje_descuento_2}% en un monto de {monto_2} es: {descuento_2}")
# Mostrar resultados de las compras
print(f"Compra 1: Monto total: ${monto_1:.2f}, Descuento: ${monto_1 * 0.10:.2f}, Monto final: ${monto_1:.2f}")
print(f"Compra 2: Monto total: ${monto_2:.2f}, Descuento: ${monto_2 * 0.15:.2f}, Monto final: ${monto_2:.2f}")
print(f"Descuento con el {porcentaje_descuento_2}% en un monto de {monto_2} es: {descuento_2}")
