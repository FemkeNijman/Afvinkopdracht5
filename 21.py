import random

def randomgetalmaken():
    """maakt een random getal tussen de 1 en 3
    
    input:
    output:
    return randomgetal - int
    """
    randomgetal = random.randint(1,3)
    return randomgetal

def voorwerp(randomgetal):
    """linkt het random getal aan een string
    
    input: 
    randomgetal - int
    output: 
    return computer - string
    """
    computer = str(" ")
    if randomgetal == 1:
        computer = ("Steen")
    elif randomgetal == 2:
        computer = ("Papier")
    else:
        computer = ("Schaar")
    return computer

def uitkomstbekijken(computer, eigenvoorwerp):
    """kijkt of de user of de computer wint.
    
    input: 
    computer, eigenvoorwerp - string
    output: 
    """
    if computer == eigenvoorwerp:
        print ("Gelijkspel")
    elif computer == "Schaar" and eigenvoorwerp == "Papier":
        print("Computer wint")
    elif computer == "Papier" and eigenvoorwerp == "Steen":
        print ("Computer wint")
    elif computer == "Steen" and eigenvoorwerp == "Schaar":
        print ("Computer wint")
    else:
        print ("Jij wint")

 
def main():
    randomgetal = randomgetalmaken()
    computer = voorwerp(randomgetal)
    eigenvoorwerp = str(input("Steen, papier of schaar? "))
    uitkomstbekijken(computer, eigenvoorwerp)
    while computer == eigenvoorwerp:
        randomgetal = randomgetalmaken()
        computer = voorwerp(randomgetal)
        eigenvoorwerp = str(input("Steen, papier of schaar? "))
        uitkomstbekijken(computer, eigenvoorwerp)
main()
