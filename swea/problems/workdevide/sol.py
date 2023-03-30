import sys
sys.stdin = open('input.txt')

def devide(n):
    global result, temp
    if temp < result:
        return
    if n == N:
        if temp > result:
            result = temp
        return
    for i in range(N):
        if visited[i]:
            continue
        if arr[n][i]:
            visited[i] = 1
            temp = temp*(arr[n][i]/100)
            devide(n+1)
            visited[i] = 0
            temp = temp/(arr[n][i]/100)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    temp = 1
    devide(0)
    print(f'#{tc} {(result*100):.6f}')