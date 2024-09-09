from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def solution(board):
  answer = -1
  row = len(board)
  col = len(board[0])
  visited = [[0] * col for _ in range(row)]
  q = deque()
  for i in range(row):
    for j in range(col):
      if board[i][j] == 'R':
        visited[i][j] = 1
        q.append((i,j,0))
  
  while q:
    i, j, count = q.popleft()
    for k in range(4):
      x = 1
      while True:
        ni = i+x*di[k]
        nj = j+x*dj[k]
        if ni < 0 or ni >= row or nj < 0 or nj >= col or board[ni][nj] == 'D':
          if board[ni-di[k]][nj-dj[k]] == 'G':
            return count+1
          if not visited[ni-di[k]][nj-dj[k]]:
            visited[ni-di[k]][nj-dj[k]] = 1
            q.append((ni-di[k],nj-dj[k],count+1))
          break
        x += 1
        
  return answer
  
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))