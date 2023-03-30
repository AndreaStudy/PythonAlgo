import sys
sys.stdin = open('input.txt')

def find(idx, n):
    global cnt
    if n == K:
        cnt += 1
        return
    if n > K:
        return
    for i in range(idx, N):
        if visited[i]:
            continue
        visited[i] = 1
        find(i+1, n+nums[i])
        visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    visited = [0] * N
    cnt = 0
    find(0, 0)
    print(f'#{tc} {cnt}')