async function getPizza() {
    const orderPromise = new Promise((resolve, reject) => {
        setTimeout(() => resolve("Your pizza is on its way!"), 2000);
    });

    const orderStatus = await orderPromise;

    console.log(orderStatus);
}

getPizza();
