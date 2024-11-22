const car = {
    brand: "Toyota",
    color: "red",
    year: 2020,
    start: function () {
        console.log("The car is starting...");
    },
    stop: function () {
        console.log("The car is stopping...");
    }
};

console.log(car.brand);
console.log(car.year);

car.start();
car.stop();
