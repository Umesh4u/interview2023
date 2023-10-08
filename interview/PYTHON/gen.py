def disp(p):
	for i in range(p):
		yield i


s = disp(10)

print(next(s))



1. Memory efficient
2. Time efficient


Iterator :

Iterator is an object that can be iterated.


Generator :

Generator is an function that returns an
 object which we can iterate over (one value at a time)

 Out of memory

a = [i for i in range(0,9999999999999999999999999)]  Run this program lack of memory

a = (i for i in range(0,9999999999999999999999999))  