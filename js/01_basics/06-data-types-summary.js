// 2 types of data Types
// Primitive(it is re)
// 7 types: String, Number, Boolean, null,undefined, Symbol, BigInt

const score = 100; // Numbers
const scoreValue = 100.9; // it is also number type data

const isLoggedIn = true; //boolean
const temprature = null; //null

let email; //undefined

const id = Symbol("123");
const anotherId = Symbol("123"); //both value are same but internally its unique both are different
console.log(id, anotherId);
console.log(id == anotherId); //Symbol provide uniqueness

const bigNumber = 4534656666666654657567657n; // for bigint we had to put at last in 'n'
console.log(bigNumber, typeof bigNumber);

// non-primitive(Reference)
// objects, arrays, functions
const arr = [1, 2, 3, 4, 5, 6]; // ite return type is object

let myObj = {
  name: "kusum",
  age: 30,
}; // its return type is object

const myFunction = function () {
  console.log("Hello World");
}; // its return type is function object
console.table([typeof arr, typeof myObj, typeof myFunction]);

// ************************ Memory **************************//

// 2 types of memory available
// Stack(Primitiv)- store premitive datatypes it is return copy of variable thats why its
//                  called also call by value

let myName = "Kusum";
let fullName = myName; // here is assign copied value and change only copied value not main value
fullName = "kusum Kumari";
console.log(fullName, ",", myName);

// Heap(non-primitive)- store non-premitive data types it is return refrence of variable
//                      it means we change value anywhere it reflacts in original
//                       as well that's why its called call by reference.

let userOne = {
  name: "kusum",
  age: 30,
};

let userTwo = userOne; // here assign reference of userOne obj to userTwo
userTwo.name = "kusum Kumari"; // so we change anything into userTwo it will also reflact in UserOne object
console.log(userOne, userTwo);
