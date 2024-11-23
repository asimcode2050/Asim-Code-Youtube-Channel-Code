const myIterable = {
    [Symbol.iterator]: function () {
        let values = [10, 20, 30];
        let index = 0;
        return {
            next: function () {
                if (index < values.length) {
                    return { value: values[index++], done: false };
                }
                return { value: undefined, done: true };
            }
        };
    }
};
for (let value of myIterable) {
    console.log(value); // This will print 10, then 20, then 30
}
