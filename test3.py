def contar_palabras(texto):
    palabras = texto.lower().split()  # Divide el texto en palabras y las convierte a minúsculas
    contador = {}

    for palabra in palabras:
        palabra = palabra.strip('.,!?')  # Elimina signos de puntuación alrededor de las palabras
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    # Imprime las palabras y su frecuencia
    for palabra, frecuencia in contador.items():
        print(f"{palabra}: {frecuencia}")

# Obtener la entrada del usuario
entrada = input("Ingrese un párrafo: ")

# Llama a la función para contar las palabras y mostrar los resultados
print("Palabras distintas y su frecuencia:")
contar_palabras(entrada)
