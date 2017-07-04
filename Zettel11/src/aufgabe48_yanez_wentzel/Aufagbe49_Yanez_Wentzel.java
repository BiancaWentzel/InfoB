package aufgabe48_yanez_wentzel;

public class Aufagbe49_Yanez_Wentzel {
    static public void main(String [] x) {
        // Varianten n=100 (10.000, 10^6, 10^8 und 10^9)
        //System.out.println("S: "+Summe(100));
        //System.out.println("S: "+Summe(10000));
        //System.out.println("S: "+Summe(1000000));
        //System.out.println("S: "+Summe(100000000));
        //System.out.println("S: "+Summe(1000000000));
        System.out.println("test:"+(1.0/(2*2)));
    }

    static double Summe(int n){
        double s = 0.0;
        float eins = 1;
        for (int i = 1; i <= n; i++)
            //s += 1 / i / i;
            //s += 1 / (i * i);

            //s += 1.0 / i / i;
            //s += 1.0 / (i * i);

            //s += 1.0 / ((double) (i) * i);
            //s += 1 / (double) (i * i);

            //s += eins / i / i;
            s += 1 / (1.0 * i * i);
        return s;
    }
}
// Grenzwert: 1.6449340668482264364

// 1. Variante: Berechneter Grenzwert für alle n ist immer 1.0

// 2. Variante: Berechneter Grenzwert für n=100 und n=10000 -> 1, danach wirft der Rechner eine Exeption (/by zero)



// 3. Variante: Berechnete Grenwerte : S: 1.6349839001848923
/*                                     S: 1.6448340718480652
                                       S: 1.64493306684877
                                       S: 1.644934057834575
                                       S: 1.644934057834575*/

// 4. Variante: Berechnete Grenzwerte: S: 1.6349839001848923
/*                                     S: 1.6448340718480652
                                       S: Infinity
                                       S: Infinity
                                       S: Infinity*/

// 5. Variante: Berechnete Grenzwerte: S: 1.6349839001848923
                                /*     S: 1.6448340718480652
                                       S: 1.64493306684877
                                       S: 1.644934057834575
                                       S: 1.644934057834575*/

// 6. Variante: Berechnete Grenzwerte: S: 1.6349839001848923
                                /*     S: 1.6448340718480652
                                       S: Infinity
                                       S: Infinity
                                       S: Infinity*/

// 7. Variante: Berechnete Grenzwerte: S: 1.6349839032409363
                                /*     S: 1.644834074928367
                                       S: 1.6449330699290232
                                       S: 1.6449340609148324
                                       S: 1.6449340609148324*/

// 8. Variante: Berechnete Grenzwerte: S: 1.6349839001848923
                                /*     S: 1.6448340718480652
                                       S: 1.64493306684877
                                       S: 1.644934057834575
                                       S: 1.644934057834575*/




