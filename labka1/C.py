s=input()
def low(s):
    s2=""
    for i in s:
        if ord(i)>64 and ord(i)<91:
            s2+=chr(ord(i)+32)
        else:
            s2+=i
    return s2
print(low(s))
