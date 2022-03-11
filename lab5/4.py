import re
with open('row.txt', 'r') as f:
    x = f.read()
pattern=(r'.*[A-Z][a-z].*')
l=re.findall(pattern,x)
print(l)