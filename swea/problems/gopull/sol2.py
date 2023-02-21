### 물놀이를 가자

import sys
sys.stdin= open("input.txt")

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]
TC = int(input())
for T in range(1,TC+1):
    n,m = map(int,input().split())
    mat = []
    for i in range(n):
        mat.append(input().strip())
    water = deque([])
    land =  [[0]* m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "W":
                water.append([i,j])
                land[i][j] = 1
            else:
                land[i][j] = 0
    ww = len(water)
    res = 0
    while water:
        w = water.popleft()
        for i in range(4):
            nx = w[0] + dx[i]
            ny = w[1] + dy[i]
            if 0<= nx < n and 0<= ny <m and not land[nx][ny]:
                land[nx][ny] = land[w[0]][w[1]] + 1
                res += land[w[0]][w[1]] + 1
                water.append([nx,ny])
    print(f"#{T}",res +ww - m*n)

