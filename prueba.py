import re

lista_de_palabras = ['hola', 'esto', 'es', 'un', 'ejemplo', 'en', 'minusculas', 'Id', 'Ejemplo']

patron = r'\b[a-z]+\b'

palabras_minusculas = [palabra for palabra in lista_de_palabras if re.match(patron, palabra)]

print(palabras_minusculas)
