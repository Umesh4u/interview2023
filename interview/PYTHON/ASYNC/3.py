

async with aiofiles.open('172.29.11.20_22', mode='r') as f:
	contents = await f.read()
print(contents)
