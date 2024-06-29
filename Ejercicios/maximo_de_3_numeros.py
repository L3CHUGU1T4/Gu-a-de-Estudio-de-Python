"""
Escribe un programa que encuentre el mayor de tres números ingresados por el usuario.
"""

num_1 = float(input("Ingrese el número numero 1: "))
num_2 = float(input("Ingrese el número numero 2: "))
num_3 = float(input("Ingrese el número numero 3: "))

mayor = max(num_1, num_2, num_3)

print(f"El número mas grande de los que ha ingresado es: {mayor}")