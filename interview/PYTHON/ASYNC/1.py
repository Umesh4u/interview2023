# def task1():
# 	print("Send first Email")
# 	print("First Email reply")
# 	task2()
# def task2():
# 	print('send second Email')
# 	print('second email reply')
# 	task3()
# def task3():
# 	print("Send third Email")
# 	print('Third Email reply')
# 	print("===")
# 	print("End")
# task1()


import asyncio

async def task1():
	print("Send first Email")
	asyncio.create_task(task2())
	await asyncio.sleep(1)
	print("First Email reply")
	task2()

async def task2():
	print('send second Email')
	asyncio.create_task(task3())
	await asyncio.sleep(1)
	print('second email reply')
	task3()

async def task3():
	print("Send third Email")
	await asyncio.sleep(1)
	print('Third Email reply')
	print("===")
	print("End")

asyncio.run(task1())


1. Asynchronous function in python is typically
called a 'coroutine'
2. Coroutines declared with the asnc/await syntax
3. Coroutines are special functions that return coroutine objects when called