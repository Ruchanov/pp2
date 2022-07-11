l=list(map(int,input().split()))
l2=[]
l3=[]
i=0
while i<3:
    l2.append(l[i])
    i+=1
while i<len(l):
    l3.append(l[i])
    i+=1
res=0
while len(l2)!=0:
    res+=max(l2)*max(l3)
    l2.pop(l2.index(max(l2)))
    l3.pop(l3.index(max(l3)))
print(res)