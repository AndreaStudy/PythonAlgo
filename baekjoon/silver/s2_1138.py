import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
arr = [0] * N

for i in range(N):
  count = 0
  for j in range(N):
    if arr[j] == 0 and count == lst[i]:
      arr[j] = i + 1
      break
    elif arr[j] == 0:
      count += 1
      
print(*arr)
      