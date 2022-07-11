import re
with open('raw.data', 'r') as f:
    x = f.read()
l=[]
pattern=(r'def\s(\w+)')
l=re.findall(pattern,x)
print(l)