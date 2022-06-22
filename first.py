# Q1). Python program to remove given character from String.

str_a = str(input())
print("char to remove")
a = str(input())

new_str = ""

for i in range(len(str_a)):
	if str_a[i] != a:
		new_str = new_str + str_a[i]

print (new_str)
