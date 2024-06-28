import asyncio
import time


async def foo():
	for i in range(10):
		await asyncio.sleep(1)
		print(i)



async def main():
	print("Hello world")
	print(f"Start Time at {time.strftime('%X')}")

	await foo()
	print(f"End Time at {time.strftime('%X')}")





asyncio.run(main())