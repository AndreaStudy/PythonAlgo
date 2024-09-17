def solution(k, dungeons):
  global visited, answer
  answer = 0
  visited = [0] * len(dungeons)
  print(visited)
  dfs(k, 0, dungeons) 
  return answer

def dfs(k, cnt, dungeons):
  global answer
  if cnt > answer:
    answer = cnt
  for i in range(len(dungeons)):
    if not visited[i] and k >= dungeons[i][0]:
      visited[i] = 1
      dfs(k-dungeons[i][1], cnt+1, dungeons)
      visited[i] = 0