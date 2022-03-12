import re
with open('row.txt', 'r') as f:
    x = f.read()
print(re.sub('([a-z0-9])([A-Z])', r'\1_\2', x).lower())