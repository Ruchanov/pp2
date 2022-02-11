a=input()
if len(a)>=3:
    x,y=map(int,a.split())
    l=list()
    for i in range(x):
        l.append(y+2*i)
    z=l[0]
    for i in range(1,len(l)):
        z=z^l[i]
    print(z)
else:
    b=int(a)
    c=int(input())
    l=list()
    for i in range(b):
        l.append(c+2*i)
    z=l[0]
    for i in range(1,len(l)):
        z=z^l[i]
    print(z)
