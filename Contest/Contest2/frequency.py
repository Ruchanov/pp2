s=input()
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=""
for a,b in sorted(d.items(),key=lambda x: x[1],reverse=True):
    while b>0:
        l+=a    
        b-=1
print(l)