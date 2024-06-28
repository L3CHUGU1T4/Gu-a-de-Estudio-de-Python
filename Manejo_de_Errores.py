try:
    x = float(input("Enter a number: ")) #intenta convertir la entrada del usuario a un número flotatnte
    y = float(input("Enter a number to divide by: ")) # intenta convertir la entrada del usuario a un número flotante
    result = x / y #intenta dividir x por y
    print(f"The answer is {result}") # Imprime el resultado de la división.
except ZeroDivisionError: #Maneja el eror de división por cero
    print("You tried to divide by cero!.")
except ValueError: # Maneja el error de valor inválido (no se puede convertir  flotante)
    print("You did not enter a valid number!")
finally: #Este bloque siempre se ejecuta
    print("Thank You for using the division feature.")