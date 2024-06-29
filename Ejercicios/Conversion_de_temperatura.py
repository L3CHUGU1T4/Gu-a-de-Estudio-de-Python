"""
Escribe un programa que convierta una temperatura dada en Celsius a Fahrenheit y viceversa.
"""

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Función para convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Solicitar al usuario la temperatura y la unidad
temperatura = float(input("Ingrese la temperatura: "))
unidad = input("Ingrese la unidad de la temperatura (C para Celsius, F para Fahrenheit): ").strip().upper()

# Realizar la conversión
if unidad == 'C':
    # Convertir de Celsius a Fahrenheit
    resultado = celsius_a_fahrenheit(temperatura)
    print(f"{temperatura} grados Celsius son {resultado} grados Fahrenheit.")
elif unidad == 'F':
    # Convertir de Fahrenheit a Celsius
    resultado = fahrenheit_a_celsius(temperatura)
    print(f"{temperatura} grados Fahrenheit son {resultado} grados Celsius.")
else:
    print("Unidad no reconocida. Por favor ingrese C para Celsius o F para Fahrenheit.")
