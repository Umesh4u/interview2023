import asyncio
import time

async def count():
	print("one")
	await asyncio.sleep(1)
	print("two")


async def main():
	await asyncio.gather(count(),count())


s = time.perf_counter()
asyncio.run(main())
elasped = time.perf_counter() - s
print(elasped)