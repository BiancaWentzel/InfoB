# Aufgabenzettel 8, Informatik B
# Elena Schmidt Yanez, Bianca Wentzel
# Aufgabe 39

######################################################################################################################
#                                           Aufgabe 39a: arithmetische Operationen                                   #
######################################################################################################################
# Error bei ungültigen Operanden
class AusdruckError(TypeError):
    pass

class Ausdruck:
    def __init__(self,operator,op1=None,op2=None):
        self.operator=operator
        self.operand1=op1
        self.operand2=op2

    def __str__(self):
        result = ""
        if isinstance(self.operand1,Ausdruck):
            result += "(" + str(self.operand1) + ")"
        else:
            result+= str(self.operand1)

        result+=self.operator

        if isinstance(self.operand2,Ausdruck):
            result += "(" + str(self.operand2) + ")"
        else:
            result+= str(self.operand2)

        return result

    def berechne(self):
        linkesErgebnis=0
        rechtesErgebnis=0

        if isinstance(self.operand1,Ausdruck):
            linkesErgebnis=self.operand1.berechne()
        else:
            linkesErgebnis=self.operand1

        if isinstance(self.operand2, Ausdruck):
            rechtesErgebnis = self.operand2.berechne()
        else:
            rechtesErgebnis = self.operand2

        try:
            if self.operator == '+':
                return linkesErgebnis+rechtesErgebnis

            elif self.operator == '-':
                return linkesErgebnis-rechtesErgebnis

            elif self.operator == '*':
                return linkesErgebnis*rechtesErgebnis

            elif self.operator == '/':
                return linkesErgebnis/rechtesErgebnis

            else:
                raise AusdruckError("Ungültiger Operator!!!")

        except TypeError:
            raise AusdruckError("Ein Operand ist ungültig")

print("##### Aufgabe 39 a #####")
print("Ausgeben von Ausdruck (3+x)*(6/2)")
a=Ausdruck('*',Ausdruck('+',3,'x'),Ausdruck('/',6,2))
print(a)
print()

print("##### Aufgabe 39b #####")
print("Berechnung des Ausdruck (3+6)*(6/2)")
b=Ausdruck('*',Ausdruck('+',3,6),Ausdruck('/',6,2))
print("Ergebnis: ",b.berechne())
print()
print("##### Ende #####")

