import random

def randomgetalmaken():
    """
output: random getal tussen 1 en 3
"""
    randomgetal = random.randint(1,3)
    return randomgetal

def voorwerp(randomgetal):
    """
input: randomgetal

output: steen, papier of schaar
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
    """
input: computer en eigenvoorwerp

output: uitkomst
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
