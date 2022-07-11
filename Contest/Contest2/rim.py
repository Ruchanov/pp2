
a=input()
b=[]
sum=0
for i in a:
    if(i=='I'):
        b.append(1)
    elif(i=='V'):
        b.append(5)
    elif i=='X':b.append(10)
    elif i=='L':b.append(50)
    elif i=='C':b.append(100)
    elif i=='D':b.append(500)
    elif i=='M':b.append(1000)
for i in range(len(b)-1):
    if(b[i]<b[i+1]):
        b[i]*=-1
for i in b:
 sum+=i
print(sum)