def es_palindromo(cadena):
    # Eliminar espacios, signos de puntuación y convertir a minúsculas
    cadena = ''.join(e for e in cadena if e.isalnum()).lower()

    # Verificar si es un palíndromo
    return cadena == cadena[::-1]

entrada = input("Ingrese una cadena de texto: ")

if es_palindromo(entrada):
    print("Es un palindromo.")
else:
    print("No es un palindromo.")
