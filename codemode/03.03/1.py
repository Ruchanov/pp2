l=[2,3,5434,653,6532,57,32]
def is_prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
if all([is_prime(i) for i in l]):
    print('All prime')
else:
    print('not all')
