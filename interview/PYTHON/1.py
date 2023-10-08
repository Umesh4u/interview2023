import asyncio
import time

# async def main():
# 	print("Hello")
# asyncio.run(main())


async def foo():
	for i in range(10):
		await asyncio.sleep(1)
		print(i)

async def main():
	print("Welcome to python")
	print(f"started at {time.strftime('%X')}")

	await foo()
	print(f"End time at {time.strftime('%X')}")


asyncio.run(main())