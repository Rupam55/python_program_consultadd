# Q3). Python Program to check if two Strings are Anagram.

s1 = str(input())
s2 = str(input())

if(sorted(s1)== sorted(s2)):
	print("The strings are anagrams.")
else:
	print("The strings aren't anagrams.")		

