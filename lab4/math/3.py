import math
a, n = map(int, input().split())
s = (n * (a**2))/(4*math.tan((2*math.pi)/(2*n)))
print(s)