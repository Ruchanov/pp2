import re
with open('raw.data', 'r', encoding='utf-8') as f:
    x = f.read()
pattern=r'Стоимость\n(?P<Price>[\d\s]+)'
l=re.findall(pattern,x)
print(len(l),l)
arr=[int(i.replace(' ','')) for i in l]
print(sum(arr))