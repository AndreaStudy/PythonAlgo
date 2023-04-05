import sys
sys.stdin = open('input.txt')

def find(x, y, tx, ty, d):
    global prev, result, total
    ny = y + dy[d]
    nx = x + dx[d]
    if nx == tx and ny == ty:
        result = max(result, total)
        return
    if 0 > ny or N <= ny or 0 > nx or N <= nx:
        return
    if arr[ny][nx] in prev:
        return
    total += 1
    prev.append(arr[ny][nx])
    find(nx, ny, tx, ty, d)
    if d != 3:
        find(nx, ny, tx, ty, (d+1)%4)
    prev.pop()
    total -= 1

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    total = 1
    prev = []
    for i in range(N-2):
        for j in range(1, N-1):
            prev.append(arr[i][j])
            find(j, i, j, i, 0)
            prev.pop()
    if result:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} -1')