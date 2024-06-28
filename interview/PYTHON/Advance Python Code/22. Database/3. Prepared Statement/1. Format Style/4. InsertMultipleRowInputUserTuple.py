# Insert Multiple Row - Input from User - Tuple
import mysql.connector
def student_data(nm, ro, fe):
	try:
		conn= mysql.connector.connect(
			user='root', 
			password='geek', 
			host='localhost', 
			database='pdb',
			port=3306
		)
		if (conn.is_connected()):
			print('Connected')
	except:
		print('Unable to Connect')
		
	sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'
	myc = conn.cursor(prepared=True)
	n = nm
	r = ro
	f = fe
	params = (n, r, f)
	try:
		myc.execute(sql, params)
		conn.commit()		# Committing the change
		print('Row Inserted')		# Number of Row Inserted
	except:
		conn.rollback()		# Rollback the change
		print('Unable to Insert Data')
	myc.close()		# Close Cursor
	conn.close()	# Close Connection

while True:
	# Data from users
	nm = input('Enter Name: ')
	ro = int(input('Enter Roll: '))
	fe = float(input('Enter Fees: '))
	student_data(nm, ro, fe)
	ans = input('Do you want to Exit(y/n)?')
	if(ans=='y'):
		break
