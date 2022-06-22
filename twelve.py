# Q12). Write a program in Python for, In array 1-100 numbers are stored, one number is missing how do you find it.

A = []
for i in range(0,101):
    A.append(i)

A.remove(8)

total = (100)*(101)/2
sum_of_A = sum(A)
print(int(total - sum_of_A))
