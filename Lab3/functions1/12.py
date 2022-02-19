def histogram(l):
    l2=[]
    for i in range(len(l)):
        s=''
        while l[i]>0:
            s+='*'
            l[i]-=1
        l2.append(s)
    return l2
l=list(histogram(list(map(int,input().split()))))
print(*l,sep='\n')