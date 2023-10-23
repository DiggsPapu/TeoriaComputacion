from validacion_gramatica import validacion_gramatica

def cargar_gramatica(nombre_archivo):
    '''
        Este metodo sirve para hacer la lectura de archivos
        donde se encuntra la gramatica.

        Args:
            nombre_archivo (str): Archivo donde se encuentra la gramatica
        Returns:
            gramatica (list): Gramatica en un arreglo de tuplas. Verificada
            si es valida para ser tomada como gramatica
                
    '''
    gramatica = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if validacion_gramatica(linea):
                    simbolo, cuerpo = linea.split('->')
                    gramatica.append((simbolo.strip(), cuerpo.strip()))
                else:
                    print(f"Error: La producción '{linea}' no es válida.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{nombre_archivo}'.")

    return gramatica