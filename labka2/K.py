a=input()
s=""
ss=set()
for i in range(len(a)):
    if a[i].isalpha():
        s+=a[i]
    elif a[i]==" " or i==len(a) - 1:
        ss.add(s)
        s=""
print(len(ss))
print(*sorted(ss),sep='\n')