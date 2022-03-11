import re
with open('row.txt', 'r') as f:
    x = f.read()
print(re.sub("[ ,.]", ":",x))
