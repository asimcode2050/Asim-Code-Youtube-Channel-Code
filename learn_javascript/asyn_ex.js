function fetchDataFromServer() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("Data received from the server");
        }, 2000);
    });
}

async function getData() {
    console.log("Requesting data...");

    try {
        const result = await fetchDataFromServer();
        console.log(result);
    } catch (error) {
        console.log("There was an error:", error);
    }
}

getData();

