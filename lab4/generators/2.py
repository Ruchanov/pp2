def gen(a):
    n=0
    while n<=a:
        if n%2==0:
            yield n
        n+=1
print(*gen(int(input())))