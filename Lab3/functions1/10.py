def unique(l):
    l2=[]
    for i in range(len(l)):
        if l[i] not in l2:
            l2.append(l[i])
    return l2
l=list(map(str,input().split()))
print(*unique(l))