import re
with open('row.txt', 'r') as f:
    x = f.read()
pattern=(r'.*a.*b{1}')
l=re.findall(pattern,x)
print(l)
