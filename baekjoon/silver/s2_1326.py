import sys; input = sys.stdin.readline

from collections import deque
def bfs():
  q = deque([a - 1])
  visited = [0] * 10000
  visited[a - 1] = 1
  while q:
    target = q.popleft()
    for i in range(target,N, lst[target]):
      if not visited[i]:
        q.append(i)
        visited[i] = visited[target] + 1
        if i == b - 1:
          return visited[i]
        
    for i in range(target, -1, -lst[target]):
      if not visited[i]:
        q.append(i)
        visited[i] = visited[target] + 1
        if i == b - 1:
          return visited[i]
        
  return 0

N = int(input())
lst = list(map(int, input().split()))
a, b = map(int, input().split())

        
print(bfs()-1)

