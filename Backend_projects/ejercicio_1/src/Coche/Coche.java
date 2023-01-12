package Coche;

public class Coche {
    //Atributos
    int puertas;

    public Coche(int puertas){
        this.puertas = puertas;
    }

    //Comportamientos o métodos
    public int agregar_puerta(){
        this.puertas += 1;
        return this.puertas;
    }
}