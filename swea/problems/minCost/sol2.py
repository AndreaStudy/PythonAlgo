import sys
sys.stdin = open('input.txt')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def find(x, y):
    global result
    if visited[y][x] > result:
        return
    if x == N-1 and y == N-1:
        result = min(result, visited[y][x])
        return
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            continue
        if visited[ny][nx]:
            continue
        if arr[ny][nx] > arr[y][x]:
            visited[ny][nx] = visited[y][x] + arr[ny][nx] - arr[y][x] + 1
        else:
            visited[ny][nx] = visited[y][x] + 1
        find(nx, ny)
        visited[ny][nx] = 0
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = 1e10
    find(0, 0)
                
    print(f'#{tc} {result}')