def has33(l):
    res=False
    for i in range(1,len(l)):
        if l[i-1]==l[i]==3:
            res=True
            break
    return res
l=list(map(int,input().split()))
print(has33(l))