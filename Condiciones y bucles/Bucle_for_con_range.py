from random import randint # Importamos la función randint de la libreria random

for i in range(5): #Iterra 5 veces
    guess = int(input("Enter a number between 1 and 10: ")) #Le pide un número al usuario y lo convierte en entero
    randNum = randint(1,10) # genera un número aleatorio entre ekl 1 y el 10 y lo almacena en la variable guess

    if randNum == guess: #Si el número ingressado por el usuario es igual al generado aleatoriamente 
        print("We matched") #Imrime "We watched"
        break # Sale del bucle
    else: # Si el número ingresado no coincide con el númer aleatorio
        print(f"We dind't match. I choose {randNum}, try again!") # Imprime "We did no match. Try again y muestra el número aleatorio"
