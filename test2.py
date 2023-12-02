class ContadorPalabras:
    def __init__(self):
        self.contador = {}

    def contar_palabras(self, texto):
        # Dividir el texto en palabras y eliminar signos de puntuación
        palabras = texto.lower().split()
        palabras = [palabra.strip('.,!?') for palabra in palabras]

        # Contar la frecuencia de las palabras
        for palabra in palabras:
            if palabra in self.contador:
                self.contador[palabra] += 1
            else:
                self.contador[palabra] = 1

    def mostrar_resultados(self):
        # Mostrar las palabras distintas y su frecuencia
        print("Palabras distintas y su frecuencia:")
        for palabra, frecuencia in self.contador.items():
            print(f"{palabra}: {frecuencia}")

# Obtener la entrada del usuario
entrada = input("Ingrese un párrafo: ")

# Crear una instancia de la clase ContadorPalabras y contar las palabras
contador = ContadorPalabras()
contador.contar_palabras(entrada)

# Mostrar los resultados
contador.mostrar_resultados()
