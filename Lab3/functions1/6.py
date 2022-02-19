def reverse_sentence(s):
    l=list(s.split())
    l2=[]
    for i in range(len(l)-1,-1,-1):
        l2.append(l[i])
    return l2
s=input()
print(*reverse_sentence(s))