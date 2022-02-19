
def puzzle(a,b):
    return int((b-2*a)/2),int(a-(b-2*a)/2)
a,b=map(int,input().split())
x,y=puzzle(a,b)
print(f'chickens are {y},rabbits are {x}') 
