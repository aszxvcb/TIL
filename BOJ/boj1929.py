a, b = map(int, input().split())

def isPrime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if( x % i == 0 ):
            return False
    else:
        return True


arr = [x for x in range(a, b+1)]
for i in arr:
    if(isPrime(i)):
        print(i)