import sys
sys.stdin = open('input.txt')

def find(n, score, kcal):
    global result
    if kcal > L:
        return
    if n == N:
        if score > result:
            result = score
        return
    
    find(n+1, score, kcal)
    find(n+1, score+arr[n][0], kcal+arr[n][1])


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    find(0, 0, 0)
    print(f'#{tc} {result}')