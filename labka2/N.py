l=list()
while True:
    x=int(input())
    if x==0:
        break
    else:
        l.append(x)
if len(l)%2==0 :
    for i in range(len(l)//2):
        print(l[i]+l[len(l)-i-1],end=" ")
else:
    for i in range((len(l)//2)+1):
        if i==len(l)-i-1:
            print(l[i],end=" ")
        else:
            print(l[i]+l[len(l)-i-1],end=" ")

