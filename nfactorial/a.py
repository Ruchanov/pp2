x = int(input())
arr = []
#for i in range(x):
#    x = int(input())
#    arr.append(x)
arr = list(map(int,input().split()))
d = dict()
cnt = 0
for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]] += 1
    else:
        d[arr[i]] = 1
for i,j in d.items():
    cnt += j//2
print(cnt)
print(d)