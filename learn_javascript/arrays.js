let fruits = ["apple", "banana", "cherry"];

console.log(fruits[0]);
console.log(fruits[1]);

fruits.push("date");
console.log(fruits);

fruits.pop();
console.log(fruits); // Now the array is ["apple", "banana", "cherry"]

fruits.unshift("apricot");
console.log(fruits);

fruits.shift();
console.log(fruits);

let index = fruits.indexOf("banana");
console.log(index);

let hasCherry = fruits.includes("cherry");
console.log(hasCherry);

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}

