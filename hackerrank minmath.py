array = [3,4,2,5,1]
sarray=sorted(array)
mini=sarray[0]
maxi=sarray[len(sarray)-1]
maxisum=0
minisum=0
if array.count(mini)==5:
    for i in range (4):
        maxisum+=sarray[i]
    
else:   
    for i in sarray:
            if i==mini:
                  continue         
            
    
    for j in sarray:
            if j==maxi:
                  break
            minisum+=j

print(str(minisum)+" "+str(maxisum))





    