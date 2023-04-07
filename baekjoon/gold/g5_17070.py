import sys
input = sys.stdin.readline

dx = [0, 1, 1] 
dy = [1, 0, 1]
pd = [(0, 2), (1, 2), (0, 1, 2)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr[0][0] = arr[0][1] = 1
result = 0

if not arr[N-1][N-1]:
    stack = []
    stack.append((0, 1, 0))
    while stack:
        x, y, direc = stack.pop()
        if x == N-1 and y == N-1: 
            result += 1
            continue
        for d in pd[direc]: 
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if arr[nx][ny]:   
                continue
            if d == 2:  
                if arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1: 
                    break
            stack.append((nx, ny, d))
            
print(result)