x=int(input())
l=list()
for i in range(x):
    x=input()
    if x[0]=='1':
        x,y=map(str, x.split())
        l.append(y)
    if x[0]=='2':
        print(l[0], end=" ")
        l.pop(0)
