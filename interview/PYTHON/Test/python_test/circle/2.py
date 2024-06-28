import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1.27017/')

mydb = client('Employee')

information = mydb.employeeinformation

record = {
		"firstName" : 'samal kusum',
 		'lastname' : 'samal'


	}

imformation


information.insert_one(record)