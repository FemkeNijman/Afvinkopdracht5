def milesmaker(km):
    """maakt van het aantal km het aantal gelijke miles.

    input:
    km - float
    output:
    km - float
    """
    return km * 0.6214

def main():
    km = int(input("Geef het aantal km: "))
    print(milesmaker(km))
main()
                         
