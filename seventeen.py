# Q17). Write a program in Python to find second highest number in an integer array.

l1 = [1,2,3,4,5,6,7,8,9]

l2 = list(set(l1))

l2.sort()

print(l2[-2])
