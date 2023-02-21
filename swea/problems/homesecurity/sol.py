import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = N*2
    result = 0

    house = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                house.append((i,j))

    for k in range(1, K+1):
        cost = k*k + (k-1)*(k-1)
        for i in range(N):
            for j in range(N):
                cnt = 0
                for l in house:
                    x, y = l
                    if abs(i-x) + abs(j-y) < k:
                        cnt += 1
                if cnt * M >= cost:
                    result = max(result, cnt)

    print(f'#{tc} {result}')
                