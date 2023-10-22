import re

cadena = 'A C1'
letras = re.sub(r'[^a-zA-Z]', '', cadena)
print(letras)
