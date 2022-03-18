import os
s = input()
if os.path.exists(s):
    print(os.path.basename(s))
    print("\nDir name of the path:")
    print(os.path.dirname(s))