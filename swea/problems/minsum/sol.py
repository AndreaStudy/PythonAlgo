import sys
sys.stdin = open('input.txt')

dx = [1, 0]
dy = [0, 1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    stack = []
    stack.append((0,0))
    visited[0][0] = arr[0][0]
    while stack:
        x, y = stack.pop()
        if visited[N-1][N-1] and visited[N-1][N-1] < visited[y][x]:
            continue
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx >= N or ny >= N:
                continue
            if visited[ny][nx] == 0:
                visited[ny][nx] = visited[y][x]+arr[ny][nx]
            else:
                temp = visited[y][x]+arr[ny][nx]
                if temp < visited[ny][nx]:
                    visited[ny][nx] = temp
            stack.append((nx, ny))
    
    print(f'#{tc} {visited[N-1][N-1]}')