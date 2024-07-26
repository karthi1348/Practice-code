arr=[1,5,7,1]
arr.sort()
print(arr)
count = 0
sum = 6
left = 0
right = len(arr)-1
while(left==right):
    if arr[left]+arr[right]==sum:
        count+=1
    elif arr[left]+arr[right]<sum:
        left=left+1
    elif arr[left]+arr[right]>sum:
        right=right-1

print(count)



