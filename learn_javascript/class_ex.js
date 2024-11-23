class Car {
    constructor(brand, model, year) {
        this.brand = brand;  // Brand of the car
        this.model = model;
        this.year = year;
    }

    displayInfo() {
        return `${this.year} ${this.brand} ${this.model}`;
    }

    startCar() {
        return `${this.brand} ${this.model} is starting...`;
    }

    carAge(currentYear) {
        return currentYear - this.year;
    }
}
let myCar = new Car('Toyota', 'Corolla', 2020);
console.log(myCar.displayInfo());
console.log(myCar.startCar());
console.log(myCar.carAge(2024));
