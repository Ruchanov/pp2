x,y=input().split()
y=int(y)
sum=0
for i in x:
    sum+=int(i)**y
    y+=1
k=int(sum/int(x))
if k*int(x)==sum:
    print(k)
else:
    print(-1)

