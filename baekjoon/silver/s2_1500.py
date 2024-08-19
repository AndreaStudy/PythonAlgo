import sys; input = sys.stdin.readline

S, K = map(int, input().split())

a = S // K
b = S % K

result = 1
for i in range(K):
  if b:
    b -= 1
    result *= (a+1)
  else:
    result *= a
  
print(result)