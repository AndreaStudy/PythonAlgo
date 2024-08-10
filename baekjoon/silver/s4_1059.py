import sys ; input = sys.stdin.readline

L = int(input())
lst = list(map(int, input().split()))
N = int(input())

lst.sort()

if N in lst:
    print(0)
else:
    min = 0
    max = 0
    for num in lst:
        if num < N:     
            min = num
        elif num > N and max == 0:
            max = num
    max -= 1
    min += 1
    print((N-min)*(max-N+1) + (max-N))