# Zettel 9, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 42

######################################################################################################################
#                                       Aufgabe 42: Geld wechseln                                                    #
######################################################################################################################
def wieOftPasstMunzeInBetrag(muenztypen,betrag):
    '''Funktion berechnet die Anzahl, wie oft eine Münze in den gegebenen Betrag passt'''
    anzahlen = []

    # Teilen des Betrags durch Münzbetrag und speichern des Ergebnisses
    for munze in muenztypen:
        if betrag // munze != 0:
            anzahlen.append(betrag // munze)
        else:
            del muenztypen[muenztypen.index(munze)]

    return muenztypen,anzahlen

def wechseln(muenztypen,betrag):
    wechselgeld=[]

    if type(muenztypen) != list:
        raise TypeError("Bitte geben Sie eine Liste mit Münztypen an!")

    for element in muenztypen:
        if type(element) != int:
            raise TypeError("Der Münztyp muss ein Integer sein!")

    if type(betrag) != int:
        raise TypeError("Bitte geben Sie einen ganzzahligen Betrag an!")


    while betrag >0:

        muenztypen,anzahlen = wieOftPasstMunzeInBetrag(muenztypen,betrag)

        # Finden des Minimums und entprechend häufiges Eintragen in Wechselgeld
        geringsteAnzahl=min(anzahlen)
        optimaleMuenze=muenztypen[anzahlen.index(geringsteAnzahl)]

        wechselgeld.extend([optimaleMuenze]*geringsteAnzahl)

        # Aktualisieren des Betrags
        betrag-=(geringsteAnzahl*optimaleMuenze)

    return wechselgeld

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
# siehe Zettel

######################################################################################################################
#                                    Aufagbe 42c: Reihenfolge der Teilprobleme                                       #
######################################################################################################################
# Nacheinander natürlich!
# Es wäre sinnlos das Minimum der Anzahl zu bestimmen, wie oft eine Münze in den Betrag passt, wenn wir noch nicht
# berechnet haben, wie oft eine Münze ünerhaupt in den Betrag passt. Weiterhin kann der Betrag nicht aktualisiert
# werden, wenn wir die optimale Teillösung (Minimum der Anzahl) nicht bestimmt haben und dementsprechen auch nciht,
# wenn das erste Teilproblem noch nicht gelöst wurde (Bestimmen der Anzahl).

######################################################################################################################
#                                    Aufgabe 42d: Entstehung des Optimalwerts                                        #
######################################################################################################################
# Der Optimalwert ensteht durch die geirige Betrachtung unserer Münzen. Hierbei wird nicht das Maximum des
# Münzbetrages gesucht, sondern das Minimum der Anzahl, wie oft die gegebene Münze in den Betrag passt. Dadurch wird
# gewähleistet, dass das jeweilige Teilproblem immer die optimale Lösung liefert, die im Gesamten abenfalls optimal
# ist.


# Speicherbedarf des Programms
# Durch die Rekursion müssen die Listen 'anzahlen','muenztypen',betrag für jedes Teilproblem gespeichert werden.
# Dies führt zu sehr großer Speicherplatzauslastung und kann im Extremfall zum Stackoverflow führen.
# Unser Programm ist einigermaßen speicheraufwenig und hat einen Speicherbedarf von O(B)

# Ausprobieren:
print("##### Aufgabe 42 #####")
munzen=[1,2,5,10,15,30,50,100,200]
betrag=230
print("Bestes Wechselgeld für den Betrag ",betrag, "mit den Münztypen: ",munzen)
print(wechseln(munzen,betrag))

