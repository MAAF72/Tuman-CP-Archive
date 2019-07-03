def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def countdeg(n, primenum):
    faktor = 0
    for i in primenum:
        if n % i == 0 and n // i != i: faktor += 1
        if i > n: return faktor
    return faktor

primenum = primes(1000000)

n = int(input())
for a in range(n):
    l, r, k = map(int, input().split())
    jumlah = 0
    for i in range(l,r+1):
        x = countdeg(i, primenum)
        if x == k:
            jumlah += 1
            print(i)
    print("Case #{}: {}".format(a+1, jumlah))