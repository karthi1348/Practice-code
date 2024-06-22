nums1=[1,3,5]
nums2=[2,4]
def binarysearch(array, key):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        if array[mid] == key:
            return mid  
        elif array[mid] < key:
            low = mid + 1  
        else:
            high = mid - 1  

    return -1 

print(binarysearch(nums1,5))







        


