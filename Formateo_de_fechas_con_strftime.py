import datetime # Importa el módulo datetime para trabajar con fechas y horass

todayWithoutTime = datetime.datetime.today() # Obtiene la fecha y hora actual
print(f"The current date is {todayWithoutTime.strftime("%m/%d/%y")}") # Formatea la fecha actual en el formato mm/dd/yyyy y la imprime