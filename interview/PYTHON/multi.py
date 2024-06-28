import multiprocessing


def cube(num):
	print("cube : {}".format(num*num*num))

def print_square(num):
	print("Square : {}".format(num*num))


p1 = multiprocessing.Process(target=cube,args=(10,))

p2 = multiprocessing.Process(target=print_square,args=(20,))


p1.start()

p2.start()