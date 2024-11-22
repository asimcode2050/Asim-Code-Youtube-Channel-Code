let randomValue = Math.random();
console.log(randomValue);
let randomInt = Math.floor(Math.random() * 10);
console.log(randomInt);
let randomRange = Math.floor(Math.random() * 11) + 5;
console.log(randomRange);
let randomBool = Math.random() > 0.5;
console.log(randomBool);
let arr = [1, 2, 3, 4, 5];
for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
}
console.log(arr); 
