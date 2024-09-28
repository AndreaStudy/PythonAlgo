def solution(n):
  dp = [0,1,2,3,5,8] + [0] *  (n-4)
  
  for i in range(6, n+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 1234567
  
  return dp[n]
  
print()
print(solution(10))