public class Animal {
    private String name;
    private int age;
    public static final int MAX_AGE = 100;
    public Animal(String name, int age) { 
        this.name = name;
        this.age = age;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Max Age: " + MAX_AGE);
    }

    public boolean isAlive() {
        return age <= MAX_AGE;
    }
    public static void main(String[] args) {
        Animal dog = new Animal("Buddy", 5);
        dog.displayInfo(); 
        System.out.println("Is the dog alive? " + dog.isAlive());
    }
}
