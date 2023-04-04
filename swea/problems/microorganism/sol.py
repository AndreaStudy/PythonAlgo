import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    used_arr = [[0] * N for _ in range(N)]
    for _ in range(K):
        y, x, cnt, d = map(int, input().split())
        arr[y][x] = [cnt, d]
    