x=input()
y=input()
b=True 
for i in range(1,x/2+1):
    if x%i==0:
        b=False
        break
if y%2==0 and b==True:
    print("Good job!")
else:
    print("Try next time!")

