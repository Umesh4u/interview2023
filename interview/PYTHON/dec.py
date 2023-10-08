def disp(sum):
	def s(a,b):
		p = sum(a,b)
		print(p)
	return s


@disp
def sum(a,b):
	return a +b

sum(5,6)