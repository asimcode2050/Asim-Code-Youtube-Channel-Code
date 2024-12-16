/*
Car myCar = new Car();
 */
public class Car {
    String make;
    String model;
    int year;
    double fuelLevel;

    public Car(String make, String model, int year, double fuelLevel) {
        this.make = make;
        this.model = model;
        this.year = year;
        this.fuelLevel = fuelLevel;
    }

    public void drive(double distance) {
        double fuelConsumed = distance * 0.1;
        fuelLevel -= fuelConsumed;
        if (fuelLevel < 0) {
            fuelLevel = 0;
        }
        System.out.println("After driving " + distance + " km, the fuel level is now: " + fuelLevel + " liters.");
    }

    public void refuel(double amount) {
        fuelLevel += amount;
        if (fuelLevel > 50) {
            fuelLevel = 50;
        }
        System.out.println("The car has been refueled. The new fuel level is: " + fuelLevel + " liters.");
    }

    public void displayInfo() {
        System.out.println("Car Information:");
        System.out.println("Make: " + make);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
        System.out.println("Fuel Level: " + fuelLevel + " liters");
    }

    public static void main(String[] args) {
        Car myCar = new Car("Toyota", "Corolla", 2020, 50.0);
        myCar.displayInfo();
        myCar.drive(100);
        myCar.refuel(30);
        myCar.displayInfo();
    }
}
