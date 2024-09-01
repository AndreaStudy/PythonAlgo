import sys; input = sys.stdin.readline;
from collections import deque

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  graph[y][x] = 0
  
  while q:
    a, b = q.pop()
    for i in range(8):
      ny = b + dy[i]
      nx = a + dx[i]
      if nx < 0 or nx >= M or ny < 0 or ny >= N:
        continue
      if graph[ny][nx] == 1:
        q.append((nx, ny))
        graph[ny][nx] = 0

result = []

while True:
    cnt = 0
    M, N = map(int, input().split())
    if N == 0 and M == 0:
      break
    graph = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
      for j in range(M):
        if graph[i][j] == 1:
          bfs(j, i)
          cnt += 1
    result.append(cnt)

for i in result:
    print(i)