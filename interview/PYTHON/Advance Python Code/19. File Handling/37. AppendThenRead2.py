# Appending and then reading It wont overwrite existing data
f = open('student.txt', mode='a+')
print(f.tell())
f.write('Youtube')
print(f.tell())
f.seek(0)
print(f.tell())
data = f.read()
print(f.tell())
print(data)