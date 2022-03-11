import re
with open('row.txt', 'r') as f:
    x = f.read()
pattern= r''
print(re.sub(r"(\w)([A-Z])", r"\1 \2", x))