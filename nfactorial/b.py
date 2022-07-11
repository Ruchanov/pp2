x = int(input())
arr=list(map(int,input().split()))
y = int(input())
brr = list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(len(brr)):
        if arr[i] == brr[j]:
            arr.pop(i)
            brr.pop(j)
            break
print(sorted(brr))