import pandas as pd #importamos el módulo pandas para manipulación de datos

data = { #Define un diccionario con datos
    "name": ["John", "Jane", "Jim"],
    "age": [23, 29, 35]
}

df = pd.DataFrame(data) #Crea un dataframe a partir del diccionario

print(df) #Imprime el dataframe 

