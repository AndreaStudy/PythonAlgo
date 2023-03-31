import sys
sys.stdin = open('input.txt')

def dfs(n, sm):
    global ans

    if ans == 0:
        return

    if n == N:
        if sm >= B:
            ans = min(ans, sm-B)
        return
    
    dfs(n+1, sm+lst[n])
    dfs(n+1, sm)

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))

    ans = 1e10
    dfs(0, 0)
    print(f'#{tc} {ans}')