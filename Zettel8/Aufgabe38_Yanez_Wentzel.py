# Aufgabenzettel 8, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 38

######################################################################################################################
#                                                  Aufgabe 38: Halde                                                 #
######################################################################################################################

class Halde:
    def __init__(self):
        self.schl = [None] # Element 0 wird nicht verwendet
        self.werte= [None]
        self.inHalde = {}
        self.n = 0

    def vertausche(self,i,j):
        self.schl[i],self.schl[j] = self.schl[j],self.schl[i]
        w1,w2 = self.werte[j],self.werte[i]
        self.werte[i],self.werte[j] = w1,w2
        self.inHalde[w1],self.inHalde[w2] = i,j

    def einfügen(self,zustand,schlüssel):
        self.n += 1
        if self.n>=len(self.schl):
            self.schl.append(schlüssel)
            self.werte.append(zustand)
        else:
            self.schl[self.n] = schlüssel
            self.werte[self.n] = zustand
        self.inHalde[zustand] = self.n
        self.zuklein(self.n)

    def entferneMin(self):
        if self.n==0: raise ValueError
        self.vertausche(1,self.n)
        self.n -= 1
        self.zugroß(1)
        return self.werte[self.n+1], self.schl[self.n+1]

    def Schlüsselverkleinern(self,zustand,schlüssel):
        i = self.inHalde[zustand]
        self.schl[i] = schlüssel
        self.zuklein(i)

    def zugroß(self,i):
        "Element a[i] der Halde a[1..n] ist eventuell zu groß."
        kind1 = 2*i
        kind2 = 2*i+1
        if kind1>self.n: return
        if kind2>self.n:
            kind = kind1
        else:
            if self.schl[kind1]<self.schl[kind2]:
                kind=kind1
            else:
                kind=kind2
        if self.schl[i]>self.schl[kind]:
            self.vertausche(kind,i)
            self.zugroß(kind)

    def zuklein(self,i):
        "Element a[i] der Halde ist eventuell zu klein."
        if i==1: return
        eltern = i//2
        if self.schl[eltern]>self.schl[i]:
            self.vertausche(eltern,i)
            self.zuklein(eltern)

    def Anzahl_kleiner(self,k):
        '''Berechnung der Anzahl der Schlüssel in der Halde, die kleiner als der gegebenen Schlüssel k sind'''

        if type(k) != int:
            raise TypeError("Der Schlüssel muss vom Typ Integer sein!")

        counter = 1
        while self.inHalde[self.werte[counter]] < k:
            counter += 1

        print("Anzahl der Schlüssel kleiner als ",k,":",counter-1)


# Erstellen einer neuen Halde
neueHalde=Halde()
neueHalde.einfügen(11,8)
neueHalde.einfügen(8,3)
neueHalde.einfügen(12,8)
neueHalde.einfügen(9,5)
neueHalde.einfügen(1,2)
neueHalde.einfügen(25,4)

print("##### Aufgabe 38 #####")
print("Berechnung der Anzahl der Schlüssel in der Halde, die kleiner als k = 5 sind")
neueHalde.Anzahl_kleiner(5)
print("##### Ende #####")

# Begründung der Laufzeit:
# Durch das Iterieren über die Werte der Halde, erhalten wir die Schlüssel in sortierter Reihenfolge und können
# und wissen, sobald ein Schlüssel größer gleich k ist, auch alle nachfolgenden Schlüssel größer gleich k sind.
# Dadurch können wir nach m Schlüsseln abbrechen und erhalten eine Laufzeit von O(m).

