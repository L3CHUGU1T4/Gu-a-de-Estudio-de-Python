'''
Condicionales con if, elif, else
'''

numberOfDefects = int(input("Ingrese el número de defectos: ")) #Asigna el valor  a la variable numberOfDefects

if numberOfDefects < 5: # Si el número de defectos es menor que 5
    print("Perfect") #imprime perfect
elif numberOfDefects <= 10: # Si el número de defectos está entre 5 y 10
    print("Average") # Imprime Average
else: # Si el numero de defectos es mayor que 10
    print("needs improvement") # Imprime needs imrpovement