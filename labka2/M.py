l=list()
while True:
    s=input()
    if s=='0':
        break
    else:
        x,y,z=s.split()
        l.append((x,y,z))
for i in  sorted(l,key=lambda x: (x[2],x[1],x[0])):
    print(*i)