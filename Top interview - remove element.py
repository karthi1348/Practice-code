nums=[3,2,2,3]
val=3
nums1=[]
for i in range(0,len(nums)):
    if nums[i] != val:
        nums1.append(nums[i])
  
print(nums1)