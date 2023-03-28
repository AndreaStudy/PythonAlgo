import sys
sys.stdin = open('input.txt')

def findworkmax(last):
    global cnt, result
    if cnt > result:
        result = cnt
    if last == 24:
        return
    for i in range(N):
        if visited[i]:
            continue
        if works[i][0] >= last:
            cnt += 1
            visited[i] = 1
            findworkmax(works[i][1])
            cnt -= 1
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    works = [list(map(int, input().split())) for _ in range(N)]
    works.sort(key = lambda  works: (works[0], works[1]))
    visited = [0] * N
    cnt = 0
    result = 0
    findworkmax(0)
    print(f'#{tc} {result}')