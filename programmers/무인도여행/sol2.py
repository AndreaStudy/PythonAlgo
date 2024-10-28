from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(maps, i, j, n, m, visit):
    queue = deque()
    queue.append((i, j))
    visit[i][j] = 1
    area = int(maps[i][j])
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0 and maps[ny][nx] != 'X':
                visit[ny][nx] = 1
                area += int(maps[ny][nx])
                queue.append((ny, nx))
    return area

def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[0] * m for _ in range(n)]
    answer = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visit[i][j] == 0:
                answer.append(bfs(maps, i, j, n, m, visit))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]