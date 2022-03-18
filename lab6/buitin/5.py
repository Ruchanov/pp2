t= tuple(input().split())
def check(t):
    for i in range(len(t)):
        if t[i]!=True:
            return False
    return True
print(check(t))
