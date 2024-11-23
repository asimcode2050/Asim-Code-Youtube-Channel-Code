let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    city: "New York",
    hobbies: ["reading", "coding", "gaming"]
};
let personJSON = JSON.stringify(person);
console.log(personJSON);
function sendToServer(data) {
    console.log("Sending data to server:", data);
}
sendToServer(personJSON);

function receiveFromServer() {
    let receivedData = '{"name":"Alice","age":25,"city":"Paris"}';
    let parsedData = JSON.parse(receivedData);
    console.log("Received data:", parsedData);
}
receiveFromServer(); 
