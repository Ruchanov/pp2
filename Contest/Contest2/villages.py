x=int(input())
d={}
while x>0:
    village=input()
    y=int(input())
    while y>0:
        l=[]
        name,war=map(str,input().split())
        l.append(village)
        l.append(war)
        d[name]=l
        y-=1
    x-=1
w=input()
for a,b in d.items():
    if b[1]==w:
        print(f"('{a}', '{b[0]}')")