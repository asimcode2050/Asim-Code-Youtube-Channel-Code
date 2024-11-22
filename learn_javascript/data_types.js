let number = 42;
let name = "Alice";
let isStudent = true;
let unknownValue = null;
let notAssigned;
let uniqueID = Symbol('id');

let person = {
    name: "Alice",
    age: 25,
    isStudent: true
};

let numbersArray = [1, 2, 3, 4, 5];

function greet() {
    console.log("Hello!");
}

console.log(number);
console.log(name);
console.log(isStudent);
console.log(unknownValue);
console.log(notAssigned);
console.log(uniqueID);

console.log(person.name);
console.log(numbersArray[2]);
greet(); 
