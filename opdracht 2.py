def lees_inhoud(bestandsnaam):
    """Opent het bestand en haalt witregels weg
    
    input:
    bestandsnaam - string
    output:
    return header, sequentie - string
    """
    bestand = open(bestandsnaam)
    header = ""
    sequentie = ""
    for regel in bestand:
        if regel.startswith(">"):
            header += regel.rstrip()
        else:
            sequentie += regel.rstrip()
    return header, sequentie

def is_dna(sequentie):
    """Kijkt of de karakters in de sequentie overeenkomen met de nucleotiden

    input:
    sequentie - string
    output:
    return True or False
    """
    for nucleotide in sequentie:
        if nucleotide not in "ACGTN":
            return False
    return True

def knipt(sequentie, sequentieknip):
"""
input: kijkt of een stukje code in de sequentie voorkomt.

output: True of False.
"""
    if sequentieknip in sequentie:
        return True
    else:
        return False
    
def main():
    bestandsnaam = "lamaseq.fasta"
    header, sequentie = lees_inhoud(bestandsnaam)
    print(header)
    print(sequentie)
    if is_dna(sequentie) == True:
        print("Deze sequentie is een DNAsequentie")
    else:
        print("Deze sequentie is geen DNAsequentie")
    sequentieknip = input("Naar welk stukje ben je opzoek? ")
    if knipt(sequentie, sequentieknip) == True:
        print("Knipt wel")
    else:
        print("Knipt niet")
main()
