import threading


def main(a,b):
	print("Hello",a)


task1 = threading.Thread(target=main,args=[1,2])
task1.run()