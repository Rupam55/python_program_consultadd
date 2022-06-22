# Q8). Python program to replace the string space with a given character.

st = str(input())

str_new = ""

for i in range(len(st)):
    if(st[i] != " "):
        str_new = str_new + st[i]

print(str_new)