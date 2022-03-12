l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(2,int((l[i]/2)+1)):
        l=filter(lambda x:x==j or x%j,l)
print(l)