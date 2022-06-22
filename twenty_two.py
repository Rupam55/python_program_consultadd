# Q22). Python program to reverse an Array in two ways.

print("first method")

arr=[1,2,3,4,5]
l=[] 
for i in range(4,-1,-1):
    l.append(arr[i])
print(l)

print("second method")

brr = [1,2,3,4,5]
brr.reverse()
print(brr)
