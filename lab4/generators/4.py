def gen(a,b):
    while a <= b:
        yield a**2
        a+=1
a,b=map(int,input().split())
print(list(map(int,gen(a,b))))