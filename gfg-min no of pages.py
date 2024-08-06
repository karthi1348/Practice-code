arr=[15,10,19,10,5,18,7]
n=len(arr)
max1=0
m1=0
m2=0
arr1=[]

for i in range(0,n-1):
    m1=arr[i]+m1
    m2=sum(arr)-m1
    max1=max(m1,m2)
    arr1.append(max1)

print(min(arr1))

    



    




