string = 'forgeeksskeegfor'
left = 0 
right = len(string)-1
count=0

for i in range(0,len(string)-1):
    if string[left]!=string[right]:
        left+=1
        if string[left]!=string[right]:
            right-=1
    elif string[left]==string[right]:
        left+=1
        right-=1
        count=count+1

print(left,right,count)
        


    
