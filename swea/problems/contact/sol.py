import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

for tc in range(1,11):
    N, start = map(int,input().split())
    contact_list = list(map(int, input().split()))
    V = [[] for _ in range(101)]
    visited = [0] * 101
    for i in range(0, N, 2):
        V[contact_list[i]].append(contact_list[i+1])

    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        while V[now]:
            next = V[now].pop()
            if visited[next] == 0:
                visited[next] = visited[now] + 1
                queue.append(next)

    result = 0
    result_idx = 0
    for i in range(len(visited)):
        if visited[i] >= result:
            result = visited[i]
            result_idx = i

    print(f'#{tc} {result_idx}')