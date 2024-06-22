array = [1,1,2]
replace = 1
for i in range (1,len(array)):
    if array[i]!=array[i-1]:
        array[replace]=array[i]
        replace+=1

print(replace)
    
