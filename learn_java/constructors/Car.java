
public class Car {

    private String model;
    private int year;
    private double price;

    public Car() {
        model = "Unknown";
        year = 0;
        price = 0.0;
    }

    public Car(String model, int year, double price) {
        this.model = model;
        this.year = year;
        this.price = price;
    }

    public String getModel() {
        return model;
    }

    public int getYear() {
        return year;
    }

    public double getPrice() {
        return price;
    }

    public static void main(String[] args) {
        Car car1 = new Car();

        Car car2 = new Car("Tesla Model S", 2023, 79999.99);

        System.out.println("Car 1: Model = " + car1.getModel() + ", Year = " + car1.getYear() + ", Price = $" + car1.getPrice());
        System.out.println("Car 2: Model = " + car2.getModel() + ", Year = " + car2.getYear() + ", Price = $" + car2.getPrice());
    }
}
