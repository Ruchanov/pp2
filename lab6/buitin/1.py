l = list(map(int, input().split()))
res = 1
for i in range(len(l)):
    res *= l[i]
print(res)