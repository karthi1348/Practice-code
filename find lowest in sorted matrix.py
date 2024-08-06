def blackbox(matrix,value):
    n=len(matrix)
    m=len(matrix[0])
    count=0
    for i in range(n):
        for j in range(m):
            if matrix[i][j]<=value:
                count+=1
    return count
        
matrix=[[1, 3, 5],[2, 6, 9],[3, 6, 9]]

def median(matrix):
    z=(len(matrix)*len(matrix[0]))//2
    for i in matrix:
        if blackbox(matrix,i)>z:
            print(i)

median(matrix)


