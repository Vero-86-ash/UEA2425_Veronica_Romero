# Función de Bubble Sort para ordenar una lista
def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Función para mostrar la matriz de forma más clara
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Definir la matriz original
matriz = [
    [34, 12, 56],
    [90, 23, 78],
    [67, 45, 89]
]

# Mostrar la matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Solicitar al usuario el índice de la fila que desea ordenar (0, 1 o 2)
while True:
    try:
        indice_fila = int(input("\nIntroduce el número de la fila que deseas ordenar (0, 1, o 2): "))
        if 0 <= indice_fila < len(matriz):
            break
        else:
            print("Índice fuera de rango. Debes ingresar 0, 1 o 2.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Ordenar la fila seleccionada usando el algoritmo Bubble Sort
bubble_sort(matriz[indice_fila])

# Mostrar la matriz después de ordenar la fila seleccionada
print("\nMatriz después de ordenar la fila:")
mostrar_matriz(matriz)