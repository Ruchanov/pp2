s=input()
num=0
sum=0
for i in range(len(s)):
    if s[i]=='(':
        num+=1
    elif num>=2:
        sum=1
        num-=1
        while num>0:
            sum*=3
            num-=1
        #num=0
    elif num==1:
        sum+=1
        num=0
print(sum)