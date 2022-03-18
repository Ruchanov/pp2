import os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in range(65,91):
    with open(chr(letter) +".txt", "w") as f:
      f.writelines(chr(letter))