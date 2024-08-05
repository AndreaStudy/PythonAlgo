import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
card = list(map(int, input().split()))
lst = deque(range(1, N+1))
result = 0

for i in range(M):
    while True :
        if lst[0] == card[i]:
            lst.popleft()
            break
        else :
            if lst.index(card[i]) <= len(lst) // 2 :
                lst.rotate(-1)
            else :
                lst.rotate(1)
        result += 1
        
print(result)