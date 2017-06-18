# Zettel 9, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 42

######################################################################################################################
#                                     Aufgabe 42a) Teilprobleme des Geldwechselns                                    #
######################################################################################################################
# Teilprobleme des Geldwechselproblems

# 1. Teilproblem:
# Bestimmen, wie oft jede Münzart in den aktuellen Betrag passt

# 2. Teilproblem:
# Finden der Münzart, die am seltensten in den momentanen Betrag passt

# 3. Teilproblem:
# Speichern der Münze und Aktualisieren des Betrags

######################################################################################################################
#                                    Aufagbe 42b: Rekursionsgleichungen der Teilprobleme                             #
######################################################################################################################
# 1. Teilproblem: Wie oft passt eine Münzart in einen Betrag



#############################################################################################
# das Programm
def wechseln(muenztypen,betrag):
    anzahlen=[]
    wechselgeld=[]

    while betrag >0:
        # Teilen des Betrags durch Münzbetrag und speichern des Ergebnisses
        for munze in muenztypen:
            if betrag//munze != 0:
                anzahlen.append(betrag//munze)
            else:
                anzahlen.append(float("inf"))

        # Finden des Minimums und entprechend häufiges Eintragen in Wechselgeld
        geringsteAnzahl=min(anzahlen)
        optimaleMuenze=muenztypen[anzahlen.index(geringsteAnzahl)]

        wechselgeld.extend([optimaleMuenze]*geringsteAnzahl)

        # Aktualisieren des Betrags
        betrag-=(geringsteAnzahl*optimaleMuenze)

        # Lerren der Liste anzahlen
        del anzahlen[:]

    return wechselgeld

# Ausprobieren:
munzen=[1,2,5,10,15,50,100,200]
betrag=230

print(wechseln(munzen,betrag))

