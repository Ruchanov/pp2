x=int(input())
if x%2==1:
    a=[["#"]*x for i in range(x)]
    for i in range(x):
        for j in range(x):
            if i+j<x-1:
                a[i][j]='.'
    for i in range(x):
        for j in range(x):
            print(a[i][j], end="")
        print()
if x%2==0:
    a=[["#"]*x for i in range(x)]
    for i in range(x):
        for j in range(x):
            if i+j<x-1:
                a[i][j]='.'
    for i in range(x):
        for j in range(x-1,-1,-1):
            print(a[i][j], end="")
        print()

