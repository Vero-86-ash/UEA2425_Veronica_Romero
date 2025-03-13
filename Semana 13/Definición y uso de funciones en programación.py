# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    {
        "Ciudad": "Guayaquil",
        "semanas": [
            [   # Semana 1
                {"day": "Lunes", "temp": 24},
                {"day": "Martes", "temp": 31},
                {"day": "Miércoles", "temp": 32},
                {"day": "Jueves", "temp": 23},
                {"day": "Viernes", "temp": 31},
                {"day": "Sábado", "temp": 32},
                {"day": "Domingo", "temp": 25}
            ],
            [   # Semana 2
                {"day": "Lunes", "temp": 32},
                {"day": "Martes", "temp": 25},
                {"day": "Miércoles", "temp": 23},
                {"day": "Jueves", "temp": 31},
                {"day": "Viernes", "temp": 25},
                {"day": "Sábado", "temp": 30},
                {"day": "Domingo", "temp": 24}
            ],
            [   # Semana 3
                {"day": "Lunes", "temp": 30},
                {"day": "Martes", "temp": 23},
                {"day": "Miércoles", "temp": 25},
                {"day": "Jueves", "temp": 27},
                {"day": "Viernes", "temp": 31},
                {"day": "Sábado", "temp": 24},
                {"day": "Domingo", "temp": 29}
            ],
            [   # Semana 4
                {"day": "Lunes", "temp": 22},
                {"day": "Martes", "temp": 31},
                {"day": "Miércoles", "temp": 23},
                {"day": "Jueves", "temp": 30},
                {"day": "Viernes", "temp": 25},
                {"day": "Sábado", "temp": 29},
                {"day": "Domingo", "temp": 31}
            ]
        ]
    },
    {
        "Ciudad": "Quito",
        "semanas": [
            [   # Semana 1
                {"day": "Lunes", "temp": 18},
                {"day": "Martes", "temp": 17},
                {"day": "Miércoles", "temp": 19},
                {"day": "Jueves", "temp": 12},
                {"day": "Viernes", "temp": 20},  # Corregido "V:iernes"
                {"day": "Sábado", "temp": 16},
                {"day": "Domingo", "temp": 15}
            ],
            [   # Semana 2
                {"day": "Lunes", "temp": 20},
                {"day": "Martes", "temp": 25},
                {"day": "Miércoles", "temp": 19},
                {"day": "Jueves", "temp": 17},
                {"day": "Viernes", "temp": 17},
                {"day": "Sábado", "temp": 18},
                {"day": "Domingo", "temp": 20}
            ],
            [   # Semana 3
                {"day": "Lunes", "temp": 11},
                {"day": "Martes", "temp": 15},
                {"day": "Miércoles", "temp": 13},
                {"day": "Jueves", "temp": 19},
                {"day": "Viernes", "temp": 20},
                {"day": "Sábado", "temp": 18},
                {"day": "Domingo", "temp": 21}
            ],
            [   # Semana 4
                {"day": "Lunes", "temp": 25},
                {"day": "Martes", "temp": 11},
                {"day": "Miércoles", "temp": 18},
                {"day": "Jueves", "temp": 28},
                {"day": "Viernes", "temp": 15},
                {"day": "Sábado", "temp": 19},
                {"day": "Domingo", "temp": 21}
            ]
        ]
    },
    {
        "Ciudad": "Latacunga",
        "semanas": [
            [   # Semana 1
                {"day": "Lunes", "temp": 14},
                {"day": "Martes", "temp": 16},
                {"day": "Miércoles", "temp": 18},
                {"day": "Jueves", "temp": 20},
                {"day": "Viernes", "temp": 26},
                {"day": "Sábado", "temp": 10},
                {"day": "Domingo", "temp": 15}
            ],
            [   # Semana 2
                {"day": "Lunes", "temp": 18},
                {"day": "Martes", "temp": 20},
                {"day": "Miércoles", "temp": 18},
                {"day": "Jueves", "temp": 20},
                {"day": "Viernes", "temp": 15},
                {"day": "Sábado", "temp": 25},
                {"day": "Domingo", "temp": 22}
            ],
            [   # Semana 3
                {"day": "Lunes", "temp": 20},
                {"day": "Martes", "temp": 21},
                {"day": "Miércoles", "temp": 18},
                {"day": "Jueves", "temp": 23},
                {"day": "Viernes", "temp": 25},
                {"day": "Sábado", "temp": 19},
                {"day": "Domingo", "temp": 15}
            ],
            [   # Semana 4
                {"day": "Lunes", "temp": 16},
                {"day": "Martes", "temp": 21},
                {"day": "Miércoles", "temp": 19},
                {"day": "Jueves", "temp": 23},
                {"day": "Viernes", "temp": 16},
                {"day": "Sábado", "temp": 25},
                {"day": "Domingo", "temp": 18}
            ]
        ]
    }
]

#    print (f"{ciudad}:{promedio }"f")
def calcular_temperatura_promedio(temperaturas):
    """
    Calcular el promedio de temperaturas de cada ciudad.
    :param temperaturas: lista de diccionarios con los datos de las temperaturas.
    :return: Diccionario con las ciudades y su temperatura promedio.
    """

    promedios = {}

    # Iterar sobre cada ciudad en la lista
    for ciudad in temperaturas:
        total_temp = 0
        total_dias = 0

        # Iterar sobre cada semana de la ciudad
        for semana in ciudad["semanas"]:
            for dia in semana:
                total_temp += dia["temp"]  # Sumar la temperatura del día
                total_dias += 1  # Contar los días

        # Calcular el promedio de la ciudad
        promedio_ciudad = total_temp / total_dias
        promedios[ciudad["Ciudad"]] = round(promedio_ciudad, 2)  # Redondear a dos decimales

    return promedios

# Llamar a la función y mostrar los resultados
resultados = calcular_temperatura_promedio(temperaturas)

print("Promedio de temperaturas por ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°C")