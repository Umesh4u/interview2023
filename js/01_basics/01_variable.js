const id = 123;
let acountName = "Kusum Samal";
var accountPassword = "123456";
accountCity = "Delhi";
let accountState;
/*
we can not change const values. when we are define any value in const variable it means 
it was fixed we can not change. compiler not allowed to change const values
*/

// id = 4; // not allowed
accountName = "Umesh Samal";
accountPassword = "1234567";
accountCity = "noida";
console.table([id, accountName, accountPassword, accountCity, accountState]);

/*
-------Let and Var ki small story------

--starting me js aayi thi to usme koi scope ka concept nhi tha like local ya global concept
--to us time var se variable declaration hote the 
--developer ne "name" variable declare kiya or wo multiple places pr use kiya, or uski values 
  ko change kr diya to all over code me "name" variable update ho jata tha to ye issue tha.
--is issue ko resolve krne ke liye let ka concept aaya jo ki scope varaible hai.
--Var completely remove nhi kiya gya hai abhi bhi exist krtaa hai because purane code var pr hi hai.
--But modern programming me var use nhi krna cahiye.
--Scopes conflict hote hai var use krne se

*/
