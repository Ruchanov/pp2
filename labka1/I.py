x=int(input())
s="@gmail.com" 
while x>0:
    y=input()
    if s in y:
        print(y.strip(s))
    x-=1