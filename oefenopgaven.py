def mijn_functie(string1, string2) :
    uitvoer = ""
    for c in string1:
        if c in string2:
            uitvoer += c
    return uitvoer