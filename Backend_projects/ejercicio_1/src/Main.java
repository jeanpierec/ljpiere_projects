import Coche.Coche;

public class Main {
    public static void main(String[] args) {
        int p_suma = suma(1,4,6);
        System.out.println(p_suma);
        //Creacion objeto coche
        Coche bmw = new Coche(1);
        int puertas = bmw.agregar_puerta();
        System.out.println(puertas);
    }
    //Funciona suma de valores
    public static int suma(int a, int b, int c){
        return a + b + c;
    }
}