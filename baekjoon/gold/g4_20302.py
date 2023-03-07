import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
word = deque(list(input().split()))
q = []

while word:
    temp = word.popleft()
    if temp.isdigit():
        q.append(int(temp))
    else:
        if temp == '*':
            q.append(int(word.popleft())*q.pop())
        else:
            q.append(q.pop()/int(word.popleft()))

temp = q[0]
if temp == int(temp):
    print('mint chocolate')
else:
    print('toothpaste')