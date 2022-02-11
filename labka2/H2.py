x,y=map(int,input().split())
z=int(input())
l=list()
while z>0:
    dis=float(0)
    c,d=map(int,input().split())
    dis=((c-x)**2+(d-y)**2)**0.5
    l.append((dis, c, d))
    z-=1
for d,a,b in sorted(l):
    print(a,b)