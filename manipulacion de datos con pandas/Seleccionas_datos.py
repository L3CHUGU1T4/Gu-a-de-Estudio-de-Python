import pandas as pd #importamos el módulo pandas para manipulación de datos

data = { #Define un diccionario con datos
    "name": ["John", "Jane", "Jim", "Leobardo"],
    "age": [23, 29, 35, 19]
}

df = pd.DataFrame(data) #Crea un dataframe a partir del diccionario

print(df["name"]) #Selecciona la columna name del dataframe
print(df.iloc[0]) #Selecciona e imprime la primera fila del dataframe por índice
print(df[df["age"] > 25]) #Filtra las filas donde la edad es mayor a 25 y las imprime