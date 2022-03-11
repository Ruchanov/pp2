import re
with open('row.txt', 'r') as f:
    x = f.read()
print(''.join(i.capitalize() for i in x.split('_')))