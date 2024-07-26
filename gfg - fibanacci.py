
def printFibb(k):
    a=0
    b=1
    c=0   
    arr=[1]
    if k ==0:
        return None
    elif k ==1:
        return arr
    elif k>1:
        for i in range(0,k-1):
            c=a+b
            a=b
            b=c
            arr.append(c)
    return arr

print(printFibb(9))



    


    
    