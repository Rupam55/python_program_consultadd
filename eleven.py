# Q11). Python program to convert lowercase vowel to uppercase in string.

st = str(input())

new_str = ""

for i in range(len(st)):
    if(st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u' or st[i] == 'A' or st[i] == 'E' or st[i] == 'I' or st[i] == 'O' or st[i] == 'U'):
        new_str = new_str + st[i].upper()
    else:
        new_str = new_str + st[i]

print(new_str)