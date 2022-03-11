import re
with open('row.txt', 'r') as f:
    x = f.read()
l=re.findall('[A-Z][^A-Z]*', x)
print(l)