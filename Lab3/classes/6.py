def prime(a):
    res=True
    if a==2:
        return res
    for i in range(2,int(a/2)+1):
        if a%i==0:
            res=False
    return res
l=list(map(int,input().split()))
l2=filter(prime,l)
print(*l2)