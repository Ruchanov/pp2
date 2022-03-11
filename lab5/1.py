import re
with open('row.txt', 'r') as f:
    x = f.read()
pattern=(r'.*ab*.*')
l=re.findall(pattern,x)
print(l)
