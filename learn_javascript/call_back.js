function prepareCoffee(callback) {
    console.log("Preparing coffee...");
    setTimeout(() => {
        console.log("Coffee is ready!");
        callback();
    }, 2000);
}
function serveCoffee() {
    console.log("Serving coffee to the customer...");
}
prepareCoffee(serveCoffee);
