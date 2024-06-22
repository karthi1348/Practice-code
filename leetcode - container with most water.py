height = [1,8,6,2,5,4,8,3,7]
maxarea=0
left = 0
right = len(height)-1
while left < right:
    initialarea= (min(height[left],height[right])*(right-left))
    maxarea=max(maxarea,initialarea)
    if height[left]<height[right]:
        left += 1
    else:
        right -= 1

print (maxarea)


