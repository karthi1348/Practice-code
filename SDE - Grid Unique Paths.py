
def uniquepaths(m,n):
    def countpaths(i,j):
        if i==(m-1) and j==(n-1):
            return 1
        elif i>=m or j>=n:
            return 0 
        else:
            return countpaths(i+1,j)+countpaths(i,j+1)   
    return countpaths(0, 0)
    
print(uniquepaths(3,7))



    