import sys; input = sys.stdin.readline

N, L = map(int, input().split())

# L의 최대 길이 100
for i in range(L, 101):
    # N = i * (i+1) // 2
    ix = N - (i * (i+1) // 2)
    if ix % i == 0:
        x = ix // i
        if x + 1 >= 0:
            print(*(i for i in range(x+1, x+i+1)))
            break
        
else:
    print(-1)