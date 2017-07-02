package aufgabe48_yanez_wentzel;

/* Klasse Knoten, die festlegt, dass unser Knoten einen Wert hat und ein Knotenobjekt, dass auf den nächsten
 Knoten zeigt */
class Knoten {
    int wert;
    Knoten next = null; // Setzen das Knotenobjekt auf den nächsten Knoten

    Knoten(int i) {
        wert = i; // Setzen des Wertes
    }
}

// Klasse zum Verketten der Knoten -> Verkettete Liste
class VerketteteListe {
    public static void main(String [] x) {
        VerketteteListe neueListe = new VerketteteListe(); // Erzeugen einer verketteten Liste
        Knoten knoten10 = neueListe.einfuege(10);
        Knoten knoten8 = neueListe.einfuege(8);
        Knoten knoten5 = neueListe.einfuege(5);
        Knoten knoten4 = neueListe.einfuege(4);
        // Ausgabe der Verketteten Liste
        System.out.println("Erstellen einer verketteten Liste");
        neueListe.durchlaufe();
        System.out.println("");

        // Einfügen eines Knotens mit dem Wert 9 zwischen Knoten8 und Knoten10
        System.out.println("Einfügen des Knotens 9 zwischen Knoten 8 und Knoten 10");
        neueListe.einfuege(9,knoten8);
        neueListe.durchlaufe();
        System.out.println("");

        // Löschen des ersten Knotens
        System.out.println("Löschen des ersten Elements der Liste");
        neueListe.loesche();
        neueListe.durchlaufe();
        System.out.println("");

        // Löschen eines beliebigen Knotens
        System.out.println("Löschen des Knotens 8");
        neueListe.loesche(knoten8);
        neueListe.durchlaufe();
        System.out.println("##### Ende #####");
    }

    Knoten eingang; // per default null

    public Knoten einfuege(int i) {
        Knoten a = new Knoten(i);
        a.next = eingang;
        eingang = a; // neuer Knoten wird neuer Startknoten
        return a;
    }

    public void durchlaufe() {
        Knoten a = eingang;
        System.out.println("Verkettete Liste: ");
        while (a!=null) {
            System.out.print(a.wert + " ");
            a = a.next;
        }
        System.out.println("");
    }

    // Aufgabe 48 a: Eifügen eines Knotens an einer beliebigen Stelle
    public void einfuege(int i, Knoten k){
        /* Wir müssen in unserer Liste nicht nach dem Knoten k suchen, da die Methode bereits das Knotenobjekt
        übergeben bekommen hat */

        // einfuegen des Knoten nach Knoten k
        Knoten neuerKnoten = new Knoten(i);
        neuerKnoten.next = k.next; // neuer Knoten zeigt auf Knoten, auf den k vorher gezeigt hat
        k.next = neuerKnoten; // k zeigt jetzt auf den eigenfügten Knoten
    }

    // Aufgabe 48b: Löschen des ertsen Elements aus der Liste
    public boolean loesche(){
        if (eingang==null){
            return false;
        }
        eingang = eingang.next;
        return true;
        // Knotenobjekt zeigt auf den 2. Knoten, sodass der erste Knoten nicht mehr erreichbar ist
    }

    // Aufgabe 48c: Löschen eines Knotens an beliebiger Stelle
    public boolean loesche(Knoten k){
        Knoten aktuellerKnoten = eingang;
        /* solange der aktuelle Knoten nicht unserem Knoten k entspricht und wir nicht am Ende der Liste sind,
        gehen wir zum nächsten Knoten und vergleichen diesen mit unserem Knoten k */
        while (aktuellerKnoten.next!=null && !aktuellerKnoten.next.equals(k)){
            aktuellerKnoten = aktuellerKnoten.next;
        }

        if (aktuellerKnoten.next==null){
            System.out.println("Knoten nicht in der Liste enthalten!");
            return false;
        }

        /* Das Knotenobjekt unseres aktuellen Knotens zeigt auf den übernächsten Knoten, sodass der Knoten k nicht
        mehr erreichbar ist */
        aktuellerKnoten.next = aktuellerKnoten.next.next;
        return true;

    }
}

