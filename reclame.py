from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {prijs * (1 - korting)} euro."
    return uitvoer

print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    
    totaal = sum(inkomsten)
    bedrag = totaal * 0.09
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."

print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345]))

def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    bedrag = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."

print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return max(invoer_lijst), min(invoer_lijst)

print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

print(combinatie([220, 430, 125, 160, 205, 90, 345]))