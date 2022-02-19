def has007(l):
    res=False
    for i in range(2,len(l)):
        if l[i-2]==0 and l[i-1]==0 and l[i]==7:
            res=True
            break
    return res
l=list(map(int,input().split()))
print(has007(l))