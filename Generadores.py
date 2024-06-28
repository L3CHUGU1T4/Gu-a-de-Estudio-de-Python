"""
Un generador es un tipo especial de función que devuelve un objeto generador
"""

squares = (x**2 for x in range (10)) #crea un generador de los cuadrados de los números del 0 al 9

for square in squares: #Itera sobre el mismo generador
    print(square)  #imorime sobre cada cuadrado