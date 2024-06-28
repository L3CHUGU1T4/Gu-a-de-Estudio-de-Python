with open('Lectura_y_escritura_de_Archivos/file.txt','r') as file: # Abre el archivo file.txt en modo de lectura
    contents = file.read() #Lee todo el contenido del archivo.
    print(contents) #Imprime el contenido leido.