# import package
import asyncio,aiofiles
import time   			# Used for time related package
import pdb              # Used gor debugging
import csv              # Used for import csv file
import os,re
import pandas as pd
from itertools import combinations
import glob
# from async_class import AsyncClass

async def read_file(filename):
	try:
		"""
			Opens the router file and filters the ARP table data

			Parameters
			----------

			file_name : str
				The file name on the disk
			Parses the file for 'show arp' table content and exists as soon as table to data is captured.
			avoids reading conpleted file

			Returns
			_______

			DataFrame

				A dataframe contaings ARP table for the router

		"""
		arp_table = []
		arp_row_start = 0
		iternum = 0
		async with aiofiles.open(filename,mode='r') as fileobject:
			async for line in fileobject:
				iternum += 1
				if 'Hardware Addr' in line:
					arp_row_start = iternum - 1
				if arp_row_start and line == '\n':
					break
				else:
					arp_table.append(line.rstrip())
		atbl = arp_table[arp_row_start:]
		col_names = re.split(r'\s{2,}',atbl[0])
		data = [i.split() for i in atbl[1:]]
		df = pd.DataFrame(data,columns = col_names)
		ignore_cols = ['Age','Type']
		df.drop(ignore_cols,inplace=True,axis=1)
		return df
	except Exception as e:
		print("Error is read files",str(e))
		return 




async def get_project_results(projects: list):
	"""
		Opens the router file and filters the ARP table data

		Parameters
		----------

		FIle_list : list

		  The FIle name on the disk

		Parses the file for 'show arp' table content and exists as soon as table 
		to data is captured
		avoids reading completed file

		Returns
		-------

		DataFrame
			a dataframe containg ARP table for the router


	"""
	print("umesh test")
	results = await asyncio.gather(*[read_file(file_name) for file_name in projects])
	return results

def aggregate_results(projects: list):
	# document
	# print time taken to
	results = asyncio.run(get_project_results(projects))
	return results

if __name__ == '__main__':
	try:
		print("v")
		files = [f for f in os.listdir('.') if os.path.isfile(f)]

		# files = [f for f in os.listdir('.') if os.path.isfile(f)]
		files = list(filter(lambda file: file.endswith('_22'),files))
		contents = aggregate_results(files)
		arp_dict = dict(zip(files, contents))
		final_dict = {}
		file_combinations = combinations(files,2)
		for file_comb in file_combinations:
			print('File combination being matched (row by row): '+ str(file_comb[0])+ " with " + str(file_comb[1]))
			comb_name = file_comb[0].split('_')[0]+'_'+file_comb[1].split('_')[0]
			final_dict[comb_name] = []
			contents[0] = contents[0].reset_index()
			contents[1] = contents[1].reset_index()
			for index,row1 in contents[1].iterrows():
				for index,row2 in contents[0].iterrows():
					if row1['Address'] == row2['Address'] and row1['Hardware Addr']== row2['Hardware Addr'] and row1['State'] != row2['State']:
						print("umesh")
						if row1['State'] == 'Interface':
							if row2['State'] == 'Dynamic':
								final_dict[comb_name].append(row1['Interface'])
						if row1['State'] == 'Dynamic':
							final_dict[comb_name].append(row1['Interface'])
					else:
						pass
		for comb,v in final_dict.items():
			a_set = set(v)
			contents_duplicated = len(v) != len(a_set)
			print("Below are the logical connections found with ARP table data from all the filew")
			if contents_duplicated:
				conn_ips = comb.split('_')
				conninfo = "<->".join(conn_ips)
				print(conninfo)
	except Exception as e:
		print("Error in Main function",str(e))
