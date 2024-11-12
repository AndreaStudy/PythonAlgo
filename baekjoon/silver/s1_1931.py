import sys
input = sys.stdin.readline

N = int(input().rstrip())
answer = 0
time = []

for i in range(N):
  time.append(list(map(int, input().split())))
  
time.sort(key = lambda x : (x[1], x[0]))

start, end = 0, 0

for ns, ne in time:
  if ns >= end:
    answer += 1
    end = ne
    
print(answer)