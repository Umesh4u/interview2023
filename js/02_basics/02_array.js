const marvel_heros = ["thor", "ironman", "spiderman"];
const dc_heros = ["superman", "flash", "batman"];

// marvel_heros.push(dc_heros); // push method through add another list it will converted nested list and push method change original array
console.log(marvel_heros); // [ 'thor', 'ironman', 'spiderman', [ 'superman', 'flash', 'batman' ] ]

const all_heros = marvel_heros.concat(dc_heros); // by concat method both list combined perfectly but it is not changed original array
console.log(marvel_heros); // it will return original array
console.log(all_heros); // here we can see concatenated values

//spread operator
const all_new_heros = [...marvel_heros, ...dc_heros]; // here we can easily concatinate multiple arrays quickly
console.log("kkkkkkkkkkk", all_new_heros); // it will return concatinated values

const another_array = [1, 2, 3, [(4, 5)], [6, 7, [8]], 9, 10];
const real_another_array = another_array.flat(3);
console.log(real_another_array);
