import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(i):
  visited[i] = 1
  for i in lst[i]:
    if not visited[i]:
      dfs(i)


N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]

for _ in range(M):
  a,b = map(int, input().split())
  lst[a].append(b)
  lst[b].append(a)
  
  
count = 0
visited = [0] * (N+1)
for i in range(1, N+1):
  if not visited[i]:
    dfs(i)
    count += 1
    
print(count)