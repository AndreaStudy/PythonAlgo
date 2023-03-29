import sys
sys.stdin = open('input.txt')

def findCost(n):
    global total, result
    if total > result:
        return
    if n == N:
        if total < result:
            result = total
        return
    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        total += arr[n][i]
        findCost(n+1)
        visited[i] = 0
        total -= arr[n][i]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    total = 0
    result = 1e10
    findCost(0)
    print(f'#{tc} {result}')