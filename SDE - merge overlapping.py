intervals=[[1,4],[4,5]]
arr=[]
intervals.sort()
arr.append(intervals[0])

print(intervals)
print(arr)
j=0        
for i in range (1,len(intervals)):
    if arr[j][1]>=intervals[i][0]:
        arr[j][1]=max(arr[j][1],intervals[i][1])

    elif arr[j][1]<intervals[i][0]:
        arr.append(intervals[i])
        j=j+1

print(arr)


    



        
        


        


