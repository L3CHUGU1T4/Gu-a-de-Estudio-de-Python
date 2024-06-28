import datetime

date_string = "21 June, 2024" #Asigna una cadena de texto con una fecha a la variable date_string

date_object = datetime.datetime.strptime(date_string, "%d %B, %Y") #Convierte la cadena de texto a un objeto datetime utilizando el formato especificado

print(f"{date_string}")
print(f"{date_string}")