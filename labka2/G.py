x=int(input())
d=dict()
for i in range(x):
    y,z=map(str,input().split())
    d[z]=d.get(z,0)+1
k=int(input())
for i in range(k):
    y,z,q=map(str,input().split())
    if z in d.keys():
        d[z]-=int(q)
#print(f'Demons left: {sum([i for i in d.values() if i>0])}')
sum=0
for i in d.values():
    if i>0:
        sum+=i
print('Demons left: ',sum)