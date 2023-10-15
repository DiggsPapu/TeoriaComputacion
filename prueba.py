cadena = "fork|meat|soup| cat|spoon|oven|knife|juice|dog|cake|beer"

# Dividir la cadena en palabras utilizando el carácter de separación '|'
palabras = cadena.split('|')

# Eliminar los espacios en blanco al comienzo y final de cada palabra
palabras_sin_espacios = [palabra.strip() for palabra in palabras]

# Unir las palabras nuevamente en una cadena sin espacios en blanco no deseados
cadena_sin_espacios = '|'.join(palabras_sin_espacios)

print(cadena_sin_espacios)
