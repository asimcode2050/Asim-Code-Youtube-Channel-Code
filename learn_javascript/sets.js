let uniqueNumbers = new Set();
uniqueNumbers.add(10);
uniqueNumbers.add(20);
uniqueNumbers.add(10);
console.log(uniqueNumbers.size);
function addToSet(set, value) {
    set.add(value);
}
addToSet(uniqueNumbers, 30);

addToSet(uniqueNumbers, 20);
for (let number of uniqueNumbers) {
    console.log(number);
}
console.log(uniqueNumbers.has(20));
console.log(uniqueNumbers.has(40));
uniqueNumbers.delete(10);
console.log(uniqueNumbers.has(10));
uniqueNumbers.clear();
console.log(uniqueNumbers.size);
