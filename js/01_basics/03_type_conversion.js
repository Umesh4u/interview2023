let score = 33;

// console.log(typeof score);

let valueInNumber = Number(score); // any value convertion into number then we have to pass number N is capital
// console.log(typeof valueInNumber); // number data type return number which is smaller

let score1 = "33abc";
let valueInNumber1 = Number(score1);
// console.log(typeof valueInNumber1, valueInNumber1); // type is number and value is NaN

let score2 = null; // pass null value
let valueInNumber2 = Number(score2);
// console.log(typeof valueInNumber2, valueInNumber2); // type is number and value is 0

let score3 = undefined; // pass null value
let valueInNumber3 = Number(score3);
console.log(typeof valueInNumber3, valueInNumber3); // type is number and value is NaN

let isLoggedIn = " "; // empty string is false and not empty string is true
let valueIsLoggedIn = Boolean(isLoggedIn);
console.log(valueIsLoggedIn);
