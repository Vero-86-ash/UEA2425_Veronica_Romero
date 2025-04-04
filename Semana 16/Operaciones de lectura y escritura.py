# Escritura de archivo de texto
with open('my_notes.txt', 'w') as file:
    file.write(' 1: Ir a comprar arroz para el almuerzo.\n')
    file.write(' 2: Arreglar la casa.\n')
    file.write(' 3: Lamar al señor del gas.\n')
    file.write(' 4: Terminar deberes.\n ')

# Lectura de archivo de texto
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea
    for line in file:
        print(line.strip())  # strip() para eliminar saltos de línea adicionales

# No es necesario cerrar el archivo manualmente cuando usamos 'with'