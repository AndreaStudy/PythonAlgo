import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(input().strip()))
    visited = [[0]*M for _ in range(N)]
    result = 0
    queue = deque()

    for y in range(N):
        for x in range(M):
            if arr[y][x] == 'W':
                queue.append((x,y))
                visited[y][x] = 1

    length = len(queue)
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x] + 1
                result += visited[ny][nx]
                queue.append((nx, ny))

    print(f'#{tc} {result-N*M+length}')
