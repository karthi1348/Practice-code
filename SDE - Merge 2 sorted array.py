arr1=[1,2,3,0,0,0]
arr2=[2,5,6]
m=len(arr1)
n=len(arr2)
arr3=arr1+arr2
def remove_zeros(arr):
    return [x for x in arr if x != 0]
print(arr3)
arr3=remove_zeros(arr3)
arr3.sort()
print(arr3)

for i in range(0,m):
    arr1[i]=arr3[i]
k=0
for j in range(len(arr1),n):
    arr2[k]=arr3[j]
    k=k+1

print(arr1)
print(arr2)

