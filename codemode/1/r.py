import re
with open('raw.data', 'r', encoding='utf-8') as f:
    x = f.read()

pattern=r'БИН\s(\d+)'
print(re.search(pattern,x).group(1))