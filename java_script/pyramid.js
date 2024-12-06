function generatePyramid(rows) {
    for (let i = 1; i <= rows; i++) {
        let stars = "*".repeat(2 * i - 1);
        let spaces = " ".repeat(rows - i);  // ".repeat()" creates a string of spaces based on the calculated number

        console.log(spaces + stars);
    }
}
generatePyramid(5);
