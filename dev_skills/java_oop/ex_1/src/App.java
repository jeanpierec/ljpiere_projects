class FreshJuice {
    // ENUM
    enum FreshJuiceSize{ SMALL, MEDIUM, LARGE }
    FreshJuiceSize size;
}

class Puppy {

    int puppyAge; //variable to create de class

    public Puppy(String name) {
       // This constructor has one parameter, name.
       System.out.println("Passed Name is: " + name );
    }
    public void setAge( int age ) {
        puppyAge = age;
    }
  
    public int getAge( ) {
        System.out.println("Puppy's age is: " + puppyAge );
        return puppyAge;
 }
}

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("1. Hello, World!");

        // we try the new class
        FreshJuice juice = new FreshJuice(); // new object class
        juice.size = FreshJuice.FreshJuiceSize.MEDIUM; //new object
        System.out.println("2. Size: " + juice.size); //lock the value

        // Following statement would create an object myPuppy
        /* Object creation */
        Puppy myPuppy = new Puppy( "tommy" );

        /* Call class method to set puppy's age */
        myPuppy.setAge( 2 );

        /* Call another class method to get puppy's age */
        myPuppy.getAge( );

        /* You can access instance variable as follows as well */
        System.out.println("Variable Value :" + myPuppy.puppyAge );
    }
}
