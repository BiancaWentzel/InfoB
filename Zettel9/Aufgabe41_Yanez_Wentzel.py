# Zettel 9 , Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 41

######################################################################################################################
#                           Aufgabe 41a: Topologisches Sortieren, Kreis                                              #
######################################################################################################################
def TopoSort (G):
    B = set() # Menge der besuchten (beendeten) Knoten
    L = []
    S = [] # Menge der gerade (aktiven) besuchten Knoten
    def besuche(u):
        S.append(u)
        B.add(u)
        for v in G[u]:
            if v in S:
                return None # Kreis!
            if v not in B:
                besuche(v)
        L.append(u)
        S.pop()
    for v in G:
        if v not in B:
            besuche(v)
    L.reverse()
    return L

######################################################################################################################
#                           Aufgabe 41b: parallele Kanten und Schleifen                                              #
######################################################################################################################
# Wenn der Graph mehrere parallele Kanten zwischen zwei Knoten aufweist, dann muss man zwei Fälle unterscheiden:
# Sind die Kanten parrallel und gleich gerichtet, dann wird die parallele Kante ignoriert.
# Wenn unser Grapg zwischen Knoten 1 und 2 zwei parrallele Kantenzum Knoten 2 hat, dann wird im ersten Aufruf der
# Funktion besuche(Knoten), der Knoten 1 in B und S geschrieben. Dann werden alle Nachfahren des Knotens nacheinander
# durchlaufen (2 mal Knoten 2). Beim ersten Durchlauf wird geschaut, ob Knoten 2 bereits in S steht, ist dies nicht
# der Fall, schauen wir, ob Knoten 2 in B steht, wenn nicht, rufen wir die Funktion besuche mit einem neune Knoten,
# dem Knoten 2, auf.

# Sind die parallelen Kanten entgegengesetzt zueinander, dann ist keine topologische Sortierung möglich, da wir einen
# Kreis haben. (Knoten 2 steht bereits in S und würde zu einem return None führen).

# Bei einer Schleife ist ebenfalls keine topologische Sortierung möglich, da hier ebenfalls soetwas wie ein Kreis
# vorliegt und der zu besuchende Knoten bereits in der Menge der besuchten Knoten enthalten ist.
# -> return None

A = {
    "Unterhose": ["Hose"],
    "Socken": ["Schuhe"],
    "Unterhemd": ["Hose", "Hemd", "Pullover"],
    "Hemd": ["Pullover"],
    "Pullover": ["Anorak"],
    "Anorak": ["Schal"],
    "Schal": ["Socken"],
    "Hose": ["Guertel", "Schuhe"],
    "Schuhe": ["Schal"],
    "Uhr": [],
    "Guertel": []
    }

print(TopoSort(A))