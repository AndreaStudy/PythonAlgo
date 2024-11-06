import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(y, x):
    if not dp[y][x]:
        for dy, dx in dir:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if maps[ny][nx] > maps[y][x]:
                    dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
                else:
                    dp[y][x] = max(1, dp[y][x])
    return dp[y][x]


if __name__ == "__main__":
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] * N for _ in range(N)]

    dir = [[-1, 0],[1, 0],[0, -1],[0, 1]]

    for i in range(N):
        for j in range(N):
            dfs(i,j)
    
    ans = max(max(row) for row in dp)
    
    print(ans)