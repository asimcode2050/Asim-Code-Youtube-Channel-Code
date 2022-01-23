const readline = require('readline');
const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

reader.question("Please enter your name : ", name => {
    console.log(`Hello ${name}`);
    reader.close();
});
