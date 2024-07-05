nums1=[3,1,3,4,2]
duplicate=0
print(len(nums1))
def bubbleSort(arr):
    outer_break=False
    duplicate=0
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] == arr[j + 1]:
                outer_break=True
                duplicate=arr[j]
                break
            elif arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if outer_break:
            break
        elif not swapped:
            return
    return duplicate

def duplicates1(arr):
    freq_map = {}
    result = 0
    for num in arr:
        freq_map[num] = freq_map.get(num, 0) + 1
    for key, value in freq_map.items():
        if value > 1:
            result==key
    if not result:
        result=0
    return result

print(bubbleSort(nums1))
print (duplicates1(nums1))


