import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            diff = 0
            if arr[ny][nx] > arr[y][x]:
                diff = arr[ny][nx] - arr[y][x]
            
            if visited[ny][nx]:
                if visited[ny][nx] > visited[y][x] + diff + 1:
                    visited[ny][nx] = visited[y][x] + diff + 1
                else:
                    continue
            else:
                visited[ny][nx] = visited[y][x] + diff + 1
            q.append((nx, ny))
                
    print(f'#{tc} {visited[N-1][N-1]-1}')