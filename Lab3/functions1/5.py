from  itertools import permutations
def permutation(s):
    s2=permutations(s)
    return s2
s=permutation(input())
for i in s:
    print(*i)