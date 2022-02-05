x=input()
y=input()
l=[]
k=-1
for i in x:
    k+=1
    if i==y:
        l.append(k)
if len(l)==1:
    print(l[0])
else :
    print(l[0],l[-1])

