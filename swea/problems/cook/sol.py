import sys
sys.stdin = open('input.txt')

def dfs(n, alst, blst):
    global result
    if n == N:
        if len(alst) == M:
            asum = bsum = 0
            for i in range(M):
                for j in range(M):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            result = min(result, abs(asum-bsum))
        return
    
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    M = N//2
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 20000 * N * N
    alst = blst = []
    dfs(0, alst, blst)
    print(f'#{tc} {result}')