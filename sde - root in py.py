
def root(n,a,m,x):
    if m>=a:
        mid=a+(m-a)//2
        if pow(mid,n)==x:
            print(mid)
        elif pow(mid,n)>x:
            return root(n,a,mid-1,x)
        elif pow(mid,n)<x:
            return root(n,mid+1,m,x)
    else:
        print(-1)

root(4,0,69,69)

