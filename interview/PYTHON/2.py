import asyncio
import time

async def foo():
	for i in range(10):
		await asyncio.sleep(1)
		print(i)


async def main():
	print(f"Start time {time.strftime('%X')}")
	await foo()
	print(f"End time at {time.strftime('%X')}")

asyncio.run(main())