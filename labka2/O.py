d = {'ONE':'1',
'TWO':'2',
'THR':'3',
'FOU':'4',
'FIV':'5',
'SIX':'6',
'SEV':'7',
'EIG':'8',
'NIN':'9',
'ZER':'0'}
a=input()
b=''
for i in range(len(a)):
    if a[i:i + 3] in d.keys():
        b+= d[a[i:i + 3]]
    elif a[i] == '+':
        b+= '+'
#res = str(sum(list(map(int, b.split('+')))))
x,y=map(int,b.split('+'))
sum=str(x+y)
ans=''
for i in range(len(sum)):
    for j,q in d.items():
        if sum[i]==q:
            ans+=j
print(ans)