with open('Lectura_y_escritura_de_Archivos/file.txt', 'r') as file: # Abre el archivo file.txt en modo lectura
    first_line = file.readline() # Lee la primera línea del archivo
    print(f"la primera línea  del archivo es: {first_line}") # Imprime la primera linea leída