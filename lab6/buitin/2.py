s = input()
up = 0
low = 0
for i in s:
    if i.isupper():
        up += 1
    if i.islower():
        low += 1
print(f'upper case letters are {up}\nlower case letters are {low}') 