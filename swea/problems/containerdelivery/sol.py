import sys
sys.stdin = open('input.txt')

def findweight(weight):
    global result
    for i in range(N):
        if visited[i]:
            continue
        if container[i] <= weight:
            result += container[i]
            visited[i] = 1
            return

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)
    visited = [0] * N
    result = 0
    for i in range(M):
        weight = truck[i]
        findweight(weight)
    print(f'#{tc} {result}')