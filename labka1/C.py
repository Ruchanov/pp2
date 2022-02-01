s=input()
def low(s):
    for i in s:
        if ord(i)>64 and ord(i)<91:
            i=ord(ord(i)+32)
    print(s)
low(s)
