'''
Escribe un programa que elimine los elementos duplicados de una lista.
'''

lista = [12,23,34,45,56,78,89,90,12,23,67,90,23]

lista_sin_duplicados = list(dict.fromkeys(lista))

print(lista)
print(f"La lista sin duplicados es {lista_sin_duplicados}")
