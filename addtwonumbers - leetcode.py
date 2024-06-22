l1=[2,3,4]
l2=[4,5,6]
len1=len(l1)
len2=len(l2)
result1=0
result2=0
for i in l1:
    result1 = (result1*10) + i

for j in l2:
    result2 = result2*10 + j

final=result1+result2
array=[int(x) for x in str(final)]
reversearray=array[::-1]

return reversearray




