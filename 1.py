def milesmaker(km):
    """Maakt van het aantal km het aantal gelijke miles.

input = het aantal kms

output = het aantal miles
    """
    return km * 0.6214

def main():
    km = int(input("Geef het aantal km: "))
    print(milesmaker(km))
main()
                         
