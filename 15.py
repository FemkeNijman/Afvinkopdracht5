def calc_average():
    """Vraagt cijfers op en returnt het gemiddelde

    input = 
    cijfer - float
    output = 
    return gemiddelde
    """
    gemiddelde = 0
    for i in range(5):
        cijfer = (float(input("Geef een cijfer: ")))
        gemiddelde += cijfer
    gemiddelde = gemiddelde/5
    
    return gemiddelde

def determine_grade(gemiddelde):
    """ Kijkt welke letter bij het cijfer past

    input =
    gemiddelde - float
    output =
    """
    A = 9.0
    B = 8.0
    C = 7.0
    D = 6.0

    if gemiddelde >= A:
        print(gemiddelde, "= A")
    elif gemiddelde >= B:
        print(gemiddelde, "=B")
    elif gemiddelde >= C:
        print(gemiddelde, "=C")
    elif gemiddelde >= D:
        print(gemiddelde, "=D")
    elif gemiddelde <6.0:
        print(gemiddelde, "=F")

        
def main():
    gemiddelde = calc_average()
    print("Het gemiddelde is: ", gemiddelde)
    determine_grade(gemiddelde)
main()
    
