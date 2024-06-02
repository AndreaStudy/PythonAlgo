import sys

input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    
    diff = M - N
    
    if diff == 0 :
        print(1)
    else :
        bridge = factorial(M) // (factorial(N) * factorial(M-N))
        print(bridge)