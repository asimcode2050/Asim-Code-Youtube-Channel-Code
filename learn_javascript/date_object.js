const currentDate = new Date();

console.log("Current Date and Time: " + currentDate);

const specificDate = new Date(2024, 10, 22, 12, 0, 0);

console.log("Specific Date: " + specificDate);

const year = currentDate.getFullYear();
const month = currentDate.getMonth();
const day = currentDate.getDate();
const hours = currentDate.getHours();
const minutes = currentDate.getMinutes();
const seconds = currentDate.getSeconds();

console.log(`Year: ${year}, Month: ${month + 1}, Day: ${day}, Time: ${hours}:${minutes}:${seconds}`);

const futureDate = new Date(currentDate);
futureDate.setDate(currentDate.getDate() + 5);

console.log("5 Days Later: " + futureDate);

const isAfter = futureDate.getTime() > currentDate.getTime();

console.log("Is the future date after the current date? " + isAfter);

const parsedDate = new Date("2024-11-22T12:00:00"); // ISO 8601 format
console.log("Parsed Date: " + parsedDate);

console.log("Formatted Date: " + currentDate.toLocaleString());


