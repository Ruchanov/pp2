l=list(map(int,input().split()))
x=0
for j in range(len(l)):
    for i in range(x,l[x]+x+1):
        if l[x]+x+1>=len(l):
            print(1)
            exit()
        if l[x]+x<l[i]+i:
            x=i
print(0)
