from collections import deque
import sys; input = sys.stdin.readline


N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1
  
bfsVisited = [0] * (N+1)
dfsVisited = [0] * (N+1)
  
def dfs(v):
  dfsVisited[v] = 1
  print(v, end=' ')
  for i in range(1, N+1):
    if not dfsVisited[i] and graph[v][i] == 1:
      dfs(i)
      

def bfs(v):
  q = deque([v])
  bfsVisited[v] = 1
  while q:
    v = q.popleft()
    print(v, end=' ')
    for i in range(1, N+1):
      if not bfsVisited[i] and graph[v][i] == 1:
        q.append(i)
        bfsVisited[i] = 1
        
dfs(V)
print()
bfs(V)