from time import sleep
import math
x = int(input())
t = int(input())

def a(x,t):
    sleep(t/1000)
    return math.sqrt(x)
res = a(x,t)
print(f'Square root of {x} after {t} miliseconds is {res}')