def gen(a):
    n=0
    while n<=a:
        if n%3==0 and n%4==0:
            yield n
        n+=1
print(*gen(int(input())))