public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        int operacion = suma_pro(10, 30);
        System.out.println(operacion);
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