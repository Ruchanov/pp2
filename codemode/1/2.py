degree = 0
x=0 
a= "11"
for i in range(len(a)-1,-1,-1):
    x += 2**degree* int(a[i])
    degree += 1
print(x)