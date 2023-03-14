import sys
input = sys.stdin.readline

n = 10000

boolprime = [False, False, True] + [True, False] * ((n-1)//2)

for i in range(3, int(n**0.5), 2):
    if boolprime[i] :
        for j in range(i**2, n+1, i):
            boolprime[j] = False

T = int(input())

for i in range(T) :
    i = int(input())
    a = i//2
    b = i-a
    for j in range(10000) :
        if boolprime[a] and boolprime[b] :
            print(a, b)
            break
        a -= 1
        b = i-a