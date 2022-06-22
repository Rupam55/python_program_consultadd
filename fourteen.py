a = []

n = int(input())

for i in range(0,n):
    a.append(int(input()))

num = int(input())

for i in range(0,n):
    c = num-a[i]
    for j in range(i+1, n):
        if(c == a[j]):
            print("pair are " , a[i] , " and " , a[j])