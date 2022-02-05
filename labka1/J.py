l = list(input().split())
cnt=0
for i in l:
    for j in range(len(i)):
        cnt+=1
    if cnt>=3:
        print(i, end=" ")
    cnt=0    