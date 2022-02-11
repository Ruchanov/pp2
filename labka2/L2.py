s=input()
l=list()
for i in range(len(s)):
    if len(l)==0:
        l.append(s[i])
    elif (s[i]=='}' and l[len(l)-1]=='{') or (s[i]==')' and l[len(l)-1]=='(') or (s[i]==']' and l[len(l)-1]=='['):
        l.pop(len(l)-1)
    else:
        l.append(s[i])
if len(l)==0:
    print("Yes")
else:
    print("No")
        
