import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def maze(x, y):
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        arr[y][x] = 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if arr[ny][nx] == 3:
                return 1
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[ny][nx] == 0:
                stack.append((nx, ny))
    return 0
for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input().rstrip())) for _ in range(100)]
    stack =[]
    print(f'#{T} {maze(1,1)}')