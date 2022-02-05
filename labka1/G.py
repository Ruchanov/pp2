s=input()
x=0
k=0
for i in range(len(s)-1,-1,-1):
    x+=int(s[i])*(2**k)
    k+=1
print(x)
