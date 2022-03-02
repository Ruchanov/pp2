def gen(a):
    while a >= 0:
        yield a
        a-=1
print(*gen(int(input())))
