# Definir una matriz 3x3 con valores numéricos
matriz = [
    [14, 32, 58],
    [72, 80, 26],
    [42, 68, 80]
]

# Función que busca un valor en la matriz
def buscar_valor(matriz, valor_buscado):
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None  # Si no se encuentra el valor, devuelve None

# Definir el valor que quieres buscar y asegurarse de que es un número
while True:
    try:
        valor = int(input("Introduce el valor que deseas buscar en la matriz: "))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Llamar a la función de búsqueda
resultado = buscar_valor(matriz, valor)

# Mostrar el resultado
if resultado is not None:
    print(f"El valor {valor} se encuentra en la posición {resultado} (fila, columna).")
else:
    print(f"El valor {valor} no se encuentra en la matriz.")