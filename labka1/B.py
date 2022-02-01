s=input()
x=0
for i in s:
    x+=ord(i)
if x>300:
    print('It is tasty!')
else :
    print('Oh, no!')