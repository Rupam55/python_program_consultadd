# Q16). Write a program in Python to find largest and smallest number in array.

from cmath import inf


a = [1,2,3,4,5,6,7,8,9]

mn = inf
mx = -inf

for i in range(len(a)):
    mx = max(mx,a[i])
    mn = min(mn,a[i])

print(mx, mn)