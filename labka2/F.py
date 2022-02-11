x=int(input())
d=dict()
for i in range(x):
    y,z=map(str,input().split())
    if y not in d.keys():
        d[y]=int(z)
    else:
        d[y]+=int(z)
max=0
for i in d.values():
    if i>max:
        max=i
for a,b in sorted(d.items()):
    if max-int(b)==0:
        print(a," is lucky!")
    else:
        print(a," has to receive ",max-int(b)," tenge")