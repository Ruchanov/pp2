x=int(input())
d=dict()
for i in range(x):
    l2=[]
    l=list(map(str,input().split()))
    for i in range(1,len(l)):
        l2.append(l[i])
    l2.sort(key=lambda i: sum(map(ord,i)))
    d[l[0]]=l2
for a,b in sorted(d.items(), key=lambda i: len(d.values()),reverse=True):
    print(a,b)
