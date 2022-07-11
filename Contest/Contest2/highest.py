l=list(map(int,input().split()))
l.insert(0,0)
for i in range(1,len(l)):
    l[i]=l[i-1]+l[i]
max=0
for i in range(1,len(l)):
    if l[i]>max:
        max=l[i]
print(max)
