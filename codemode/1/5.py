import re
passwords = [
  "SDF#$%56bn",
  "987!@YHBv",
  "adilIjaks",
  "Group_1",
  "group-adin",
  "GRUPPA-DYVA"
]
pattern=r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,12}'
#l2=re.findall(pattern,passwords)
for i in passwords:
    if re.search(pattern,i):
        print("yes")
    else:
        print('no')