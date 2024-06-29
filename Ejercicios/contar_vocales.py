'''
Escribe un programa que cuente el número de vocales en una cadena.
'''

#cad = str(input("Ingrese la cadena a analizar: "))


pieces = ["king", "queen", "rook", "bishop", "knight", "pawn"]
pieces.sort()

print(pieces[-1])

suma = 24 % 5

print(suma)

quote = "A stitch in time saves nine"
print("nine" in quote)


def grade(score):
    if score >= 90:grade = "A"
    elif Score >= 80: grade = "B"
    elif score >= 70: grade = "C"
    else:grade = "F"
    return grade

print(grade)

for week in range(1,5):
    print("yous should", week*10,"minutes in", week)