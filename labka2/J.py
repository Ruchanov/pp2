x=int(input())
l=list()
l2=list()
l3=list()
upletter=False
lowletter=False
num=False
for i in range(x):
    l.append(input())
for i in l:
    if i not in l2:
        l2.append(i)
for i in l2:
    for j in i:
        if j>='a' and j<='z':
            lowletter=True
        if j>='A' and j<='Z':
            upletter=True
        if j>='0' and j<='9':
            num=True
    if lowletter and upletter and num:
        l3.append(i)
    upletter=False
    lowletter=False
    num=False
print(len(l3))
for i in sorted(l3):
    print(i)
