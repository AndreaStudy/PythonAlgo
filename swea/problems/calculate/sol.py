import sys
sys.stdin = open('input.txt')

from collections import deque

def calculate():
    global result
    while q:
        idx, cnt = q.popleft()
        if idx == M:
            result = cnt
            return 
        for i in range(4):
            if i == 0:
                if idx + 1 <= 1000000 and visited[idx+1] == 0:
                    q.append((idx+1, cnt+1))
                    visited[idx+1] = 1
            elif i == 1:
                if 1 <= idx - 1 and visited[idx-1] == 0:
                    q.append((idx-1, cnt+1))
                    visited[idx - 1] = 1
            elif i == 2:
                if idx * 2 <= 1000000 and visited[idx*2] == 0:
                    q.append((idx*2, cnt+1))
                    visited[idx * 2] = 1
            elif i == 3:
                if 1 <= idx - 10 and visited[idx-10] == 0:
                    q.append((idx-10, cnt+1))
                    visited[idx - 10] = 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    visited = [0] * 1000001
    q = deque()
    q.append((N,0))
    calculate()
    print(f'#{tc} {result}')