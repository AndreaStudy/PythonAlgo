import sys
sys.stdin = open('input.txt')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def find(x, y, used):
    global result, cnt, K
    
    result = max(result, cnt)
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if arr[ny][nx] < arr[y][x] and not visited[ny][nx]:
            visited[ny][nx] = 1
            cnt += 1
            find(nx, ny, used)
            visited[ny][nx] = 0
            cnt -= 1
        elif not used:
            for k in range(1, K+1):
                if arr[ny][nx]-k < arr[y][x]:
                    if not visited[ny][nx]:
                        visited[ny][nx] = 1
                        arr[ny][nx] -= k
                        cnt += 1
                        find(nx, ny, 1)
                        visited[ny][nx] = 0
                        arr[ny][nx] += k
                        cnt -= 1

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = []
    target = 0
    for i in range(N):
        arr.append(list(map(int, input().split())))
        target = max(target, *arr[i])
    visited = [[0] * N for _ in range(N)]
    
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == target:
                cnt = 1
                visited[i][j] = 1
                find(j, i, 0)
                visited[i][j] = 0
                        
    print(f'#{tc} {result}')
    
    