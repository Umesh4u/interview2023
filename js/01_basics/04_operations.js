console.log("1" + 2); //12
console.log(1 + "2"); //12
console.log("1" + 2 + 2); // 122
console.log(1 + 2 + "2"); //32

let num1, num2, num3;
num1 = num2 = num3 = 2 + 2;
console.log(num1, num2, num3);
let gameCounter = 100;
let a = gameCounter++; //postfix it is not returning incremented value because it is updated after that
console.log(a, gameCounter);
a = ++gameCounter; //prefix it is return value after increment
console.log(a);

//Study Link
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Increment
