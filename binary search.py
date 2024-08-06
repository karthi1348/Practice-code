arr=[1,2,3,4,5,6,7,8,9]
def bs(arr,start,end,x):
    mid=start+(end-start)//2
    if end>=start:
        if arr[mid]==x:
            print("answer present")
        elif arr[mid]>x:
            bs(arr,start,mid-1,x)
        elif arr[mid]<x:
            bs(arr,mid+1,end,x)
    else:
        print("answer not present")


bs(arr,0,len(arr)-1,10)
