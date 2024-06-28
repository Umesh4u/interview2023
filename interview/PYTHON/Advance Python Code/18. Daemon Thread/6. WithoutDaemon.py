from threading import Thread, current_thread
from time import sleep
def teacher():
	for i in range(1, 11):
		print('Teaching Session', i)
		sleep(1)
		
t1 = Thread(target=teacher)						# Non-Daemon Thread
t1.start()
sleep(6)
print('Exam Finished', current_thread().name)	# Non-Daemon Thread
