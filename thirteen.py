# Q13). Write a program in Python for, In a array 1-100 multiple numbers are duplicates, how do you find it.

A = []
for i in range(0,91):
    A.append(i)

for i in range(0,11):
    A.append(i)

new_dict, new_list = {}, []
 
for i in A:
    if not i in new_dict:
        new_dict[i] = 1
    else:
        new_dict[i] += 1
 
for key, values in new_dict.items():
    if values > 1:
        new_list.append(key)

print(new_list)