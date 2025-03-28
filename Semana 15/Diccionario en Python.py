# Crear diccionario inicial
informacion_personal = {
    "nombre": "Veronica Romero",
    "edad": 38,
    "ciudad": "Quito",
    "profesion": "Costurera"
}

# Acceder y Modificar Valores

# Acceder al valor de "ciudad" y modificarlo
ciudad_actual = informacion_personal["ciudad"]
print(f"La ciudad actual es: {ciudad_actual}")

informacion_personal["ciudad"] = "Ibarra"
print(f"La ciudad modificada es: {informacion_personal['ciudad']}")

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Licenciada"
print(f"La profesión actualizada es: {informacion_personal['profesion']}")

# Verificar Existencia de Claves

# Verificar si la clave "telefono" existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0983443420"
    print("Se agregó la clave 'telefono' al diccionario.")
else:
    print("La clave 'telefono' ya existe en el diccionario.")


# Imprimir el Diccionario Final
print("\nEl diccionario final es:")
print(informacion_personal)