""" archivo = open('../restaurante2.txt')
print(archivo.read()) """

try:
    with open('../restaurante2.txt', 'r') as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no fue encontrado.")
except PermissionError:
    print("No tienes permisos para leer el archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")