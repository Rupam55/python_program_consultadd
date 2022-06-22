# Q2). Python Program to count occurrence of a given characters in string.

str_a = str(input())
print("char to count")
a = str(input())

count = 0

for i in range(len(str_a)):
	if str_a[i] == a:
		count = count+1

print (count)