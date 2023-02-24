import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def connect(d, nx, ny):
    if d == 0 and underground[ny][nx] in [1,3,6,7]:
        return True
    elif d == 1 and underground[ny][nx] in [1,3,4,5]:
        return True
    elif d == 2 and underground[ny][nx] in [1,2,4,7]:
        return True
    elif d == 3 and underground[ny][nx] in [1,2,5,6]:
        return True
    else:
        return False

# 오 왼 아 위
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T+1):
    # N, M 지하 터널의 세로 가로 | R, C 맨홀 뚜껑의 세로 가로 위치 | L 탈춯 후 소요시간
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((C, R))
    # underground 값 1: 4방향, 2: 위아래, 3: 좌우, 4: 위오, 5: 오아, 6: 왼아, 7: 왼위
    visited[R][C] = 1
    while queue:
        x, y = queue.popleft()
        if visited[y][x] < L:
            if underground[y][x] == 1:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
            elif underground[y][x] == 2:
                for d in [2,3]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
            elif underground[y][x] == 3:
                for d in [0,1]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
            elif underground[y][x] == 4:
                for d in [0,3]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
            elif underground[y][x] == 5:
                for d in [0,2]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
            elif underground[y][x] == 6:
                for d in [1,2]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
            elif underground[y][x] == 7:
                for d in [1,3]:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < M and 0 <= ny < N:
                        if connect(d, nx, ny) and visited[ny][nx] == 0:
                            visited[ny][nx] = visited[y][x] +1
                            queue.append((nx, ny))
        else:
            break
    
    result = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                result += 1
    
    print(f'#{tc} {result}')