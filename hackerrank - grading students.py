
def addmark(num):
    count=0
    for i in range (num,100):
        if i%5==0:
            break
        count+=1
    return count

array=[73,67,38,33]
revised=[]
print(array)
for i in array:
    if i>37 and addmark(i)<3:
        a=i+addmark(i)
        revised.append(a)
    else:
        revised.append(i)
        
           
print(revised)



