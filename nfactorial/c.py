t = int(input())
while t>0:
    m = int(input())
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == m:
                print(f'{i+1} {j+1}')
                break
    t -= 1                