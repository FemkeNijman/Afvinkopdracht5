import random

def randomgetalmaken():
    """
output: een random getal tussen 0 en 100
"""
    randomgetal = random.randint(0,100)
    return randomgetal

def gelijk(randomgetal, geraden):
    """input: randomgetal en het geraden getal

output: print het antwoord
"""
    if geraden == randomgetal:
        print("Goed!")
    if geraden < randomgetal:
        print("Te laag")
    if geraden > randomgetal:
        print("Te hoog")
    if geraden < 0 or geraden > 100:
        print("Verkeerde input")

def main(): 
    randomgetal = randomgetalmaken()
    geraden = int(input("Raad een getal tussen de 0 en 100: "))
    gelijk(randomgetal, geraden)
    while geraden != randomgetal:
        geraden = int(input("Raad een nieuw getal tussen de 0 en 100: "))
        gelijk(randomgetal,geraden)
main()
