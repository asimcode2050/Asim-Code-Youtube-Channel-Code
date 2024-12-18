class Car {
    private String engineType;
    public String getEngineType() {
        return engineType;
    }

    public void setEngineType(String engineType) {
        if (engineType.equals("Electric") || engineType.equals("Gas")) {
            this.engineType = engineType;
        } else {
            System.out.println("Invalid engine type!"); 
        }
    }

public static void main(String[] args) {
        Car myCar = new Car();
        myCar.setEngineType("Electric"); // Valid value
        System.out.println("Engine Type: " + myCar.getEngineType()); // Should print "Electric"
        myCar.setEngineType("Diesel"); // Invalid value
        System.out.println("Engine Type: " + myCar.getEngineType());
        myCar.setEngineType("Gas"); // Valid value
        System.out.println("Engine Type: " + myCar.getEngineType()); // Should print "Gas"
}
}
