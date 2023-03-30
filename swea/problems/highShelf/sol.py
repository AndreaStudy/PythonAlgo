import sys
sys.stdin = open('input.txt')

def find(idx, n):
    global result, flag
    if not flag:
        return
    if n == B:
        flag = False
        result = n
        return
    if n > B:
        if n < result:
            result = n
        return
    for i in range(idx, N):
        if visited[i]:
            continue
        visited[i] = 1
        find(i+1, n+heights[i])
        visited[i] = 0

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    visited = [0] * N
    result = 1e10
    flag = True
    find(0, 0)
    print(f'#{tc} {result-B}')