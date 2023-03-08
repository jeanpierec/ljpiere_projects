public class Main {
    public static void main(String[] args) {
        //---------------------------------------------------
        // Primeros pasos
        //---------------------------------------------------
        System.out.println("Hello world!");
        int operacion = suma_pro(10, 30);
        System.out.println(operacion);

        //---------------------------------------------------
        // Probemos condicionales
        //---------------------------------------------------
        String estacion = "Primavera";

        if(estacion == "Primavera"){
            System.out.println("es primavera");
        } else if(estacion== "Verano"){
            System.out.println("es verano");
        } else {
            System.out.println("entonces cual estacion es?");
        }

        //---------------------------------------------------
        // Bucles
        //---------------------------------------------------
        // while
        int contador = 2;
        while(contador > 0){ // Se evalua y luego se ejecuta
            System.out.println(contador);
            contador--;
        }

        // do while
        int contador2 = 0;
        do{
            System.out.println(contador);
        } while (contador2 > 0); // Primero va la ejecución y luego se evalua
    }
    // Una función algo... particular
    public static void suma(int a, int b) {
        int resultado = 0;
        resultado = a + b;

        System.out.println(resultado);
    }
    // Cambios el retorno de la función
    public static int suma_pro(int a, int b) {
        int resultado = 0;
        resultado = a + b;

        return resultado;
    }
}