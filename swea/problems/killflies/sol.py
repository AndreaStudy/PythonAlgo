import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for y in range(N):
        for x in range(N):
            row_cnt = 0
            x_cnt = 0
            for k in range(M):
                if k == 0:
                    row_cnt += arr[y][x]
                    x_cnt += arr[y][x]
                else:
                    if y+k < N:
                        row_cnt += arr[y+k][x]
                        if x+k < N:
                            x_cnt += arr[y+k][x+k]
                        if x-k >= 0:
                            x_cnt += arr[y+k][x-k]
                    if y-k >= 0:
                        row_cnt += arr[y-k][x]
                        if x+k < N:
                            x_cnt += arr[y-k][x+k]
                        if x-k >= 0:
                            x_cnt += arr[y-k][x-k]
                    if x+k < N:
                        row_cnt += arr[y][x+k]
                    if x-k >= 0:
                        row_cnt += arr[y][x-k]
            if result < max(row_cnt,x_cnt):
                result = max(row_cnt, x_cnt)

    print(f'#{tc} {result}')

