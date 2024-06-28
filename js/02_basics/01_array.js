const myArr = [0, 1, 2, 3, 4, 5];

const myArr2 = new Array(1, 2, 3, 4, 5, 6); // 2nd way of declaration array
console.log(typeof myArr2); // array return type is object

//Array Methods

myArr.push(6); //added 6 in the last
myArr.pop(); //remove last element from the array

myArr.unshift(9); // it will add 9 in the starting array or shift all values one index ahead
console.log(myArr); // output:- [9,0,1,2,3,4,5]

myArr.shift(); // it will remove fisrt value from the array
console.log(myArr); //output:- [0,1,2,3,4,5]

console.log(myArr.includes(9)); //it will ask 9 is available or not its return boolean
console.log(myArr.indexOf(3)); //it will return index of 3

const newArr = myArr.join(); // join method will join whole array into one string
console.log(myArr);
console.log(typeof newArr); // it will return string, "0,1,2,3,4,5"

//slice and Splice
console.log("A", myArr);

const myn1 = myArr.slice(1, 3); //it is copy particular portion and return sub-array. not impact on original array
console.log(myn1); //[1,2]
console.log("B", myArr); //[0,1,2,3,4,5]

const myn2 = myArr.splice(1, 3); // it is cut out 1 to 3 portion from the array and return 1 to 3 values
console.log(myn2); // it is include end index as well [1,2,3]
console.log("C", myArr); // original array will impact splice value remove from the array, [0,4,5]
