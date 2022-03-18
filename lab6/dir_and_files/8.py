import os
path = input()
if os.access(path,os.F_OK):
    os.remove('for_del.txt')
    print('Deleted')
else:
    print('does not exist')