# Q4). Python program to check a String is palindrome or not.

def func(s):
	return s == s[::-1]

s = str(input())
ans = func(s)

if ans:
	print("Yes it is a palindrome")
else:
	print("No it not a palindrome")
