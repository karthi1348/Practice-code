array = [
    [1, 2, 3],
    [4, 5, 6],
    [9, 8, 9]
]

sum1 = 0
sum2=0
length = len(array)
a=length
b=0
for x in range (0,length):
    sum1+=array[x][x]
    sum2+=array[x][length-1-x]
    

difference = abs(sum1-sum2)
print(sum1)
print(sum2)
print(difference)
