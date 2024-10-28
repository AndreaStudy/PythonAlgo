import sys
sys.setrecursionlimit(10**9)

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(maps, i, j, n, m, visit):
    visit[i][j] = 1
    area = int(maps[i][j])

    for dx, dy in d:
        y, x = i + dy, j + dx
        if 0 <= x < m and 0 <= y < n and not visit[y][x] and maps[y][x] != 'X':
            area += dfs(maps, y, x, n, m, visit)

    return area

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    visit = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visit[i][j]:
                answer.append(dfs(maps, i, j, n, m, visit))

    if answer:
        return sorted(answer)
    else:
        return [-1]