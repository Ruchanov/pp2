l= list(map(str,input().split()))
with open('a.txt', 'w') as f:
    for i in l:
        f.write(i)
        f.write('\n')