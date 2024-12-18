public class Person {
    public String name;
    private int age;
    protected String address;
    final String birthDate = "January 1, 2000";
    public Person(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Address: " + address);
        System.out.println("Birth Date: " + birthDate);
    }

    public static void staticExample() {
        System.out.println("This is a static method. It belongs to the class, not an instance.");
    }

    public static void main(String[] args) {
        Person person = new Person("John Doe", 25, "1234 Elm Street");
        person.displayDetails();
        Person.staticExample();
    }
}
