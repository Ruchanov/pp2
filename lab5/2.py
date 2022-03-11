import re
with open('row.txt', 'r') as f:
    x = f.read()
pattern=(r'.*ab{2,3}.*')
l=re.findall(pattern,x)
print(l)