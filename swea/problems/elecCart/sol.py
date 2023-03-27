import sys
sys.stdin = open('input.txt')

def elec(n, k):
    global temp, result
    if k == N:
        if temp < result:
            result = temp
        return
    if k == N-1:
        temp += arr[n][0]
        elec(0, k+1)
        temp -= arr[n][0]
    for d in range(N):
        if not arr[n][d]:
            continue
        if visited[d]:
            continue
        else:
            visited[d] = 1
            temp += arr[n][d]
            elec(d, k+1)
            visited[d] = 0
            temp -= arr[n][d]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [1] + [0] * (N-1)
    temp = 0
    result = 1e10
    elec(0, 0)
    print(f'#{tc} {result}')
