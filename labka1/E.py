x,y=map(int,input().split())
b=True 
z=2
while z<x:
    if x%z==0:
        b=False
        break
    z+=1
if y%2==0 and b==True and x<500:
    print("Good job!")
else:
    print("Try next time!")