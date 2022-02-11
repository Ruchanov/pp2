x=int(input())
a=[[0] * x for i in range(x)]
for i in range(x):
    for j in range(x):
        if i==j:
            a[i][j]=i*j
        if i==0:
            a[i][j]=j
        if j==0:
            a[i][j]=i 
for i in range(x):
    for j in range(x):
        print(a[i][j], end=" ")
    print()
