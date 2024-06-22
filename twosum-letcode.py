array = [3,3]
length=len(array)
target=6
for x in range(0,length):
    for y in range(0,length):
        if y==x:
            continue
        elif array[x]+array[y]==target:
            twosum=[x,y]
            twosumvalue=[array[x],array[y]]
            print(f"the index - {twosum}")
            print(f"the value - {twosumvalue}")

            
        
        