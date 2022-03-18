import os
print('Exist:', os.access('c:\\Users\\ЯСЛАН\\Документы\pp2', os.F_OK))
print('Readable:', os.access('c:\\Users\\ЯСЛАН\\Документы\pp2', os.R_OK))
print('Writable:', os.access('c:\\Users\\ЯСЛАН\\Документы\pp2', os.W_OK))
print('Executable:', os.access('c:\\Users\\ЯСЛАН\\Документы\pp2', os.X_OK))