# Q18). Write a program in Python to find top two maximum number in array?

l1 = [1,2,3,4,5,6,7,8,9]

l2 = list(set(l1))

l2.sort()

print(l2[-1],l2[-2])
