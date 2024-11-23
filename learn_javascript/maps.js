let map = new Map();
map.set('name', 'John');
map.set('age', 30);
map.set(1, 'one');
map.set(true, 'yes');
let name = map.get('name');
let age = map.get('age');
let hasAgeKey = map.has('age');
let mapSize = map.size;
map.delete(1);
let newSize = map.size;
map.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});
map.clear();
let isEmpty = map.size === 0;
