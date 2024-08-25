import sys; input = sys.stdin.readline

N = int(input())
box = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
  for j in range(i):
    if box[i] > box[j] and dp[i] < dp[j] + 1:
      dp[i] = dp[j] + 1
      
print(max(dp))