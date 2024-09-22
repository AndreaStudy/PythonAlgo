import sys
sys.setrecursionlimit(10**9)

d = [0] * 100000

def fibo(n):
  if n == 2:
    return 1
  if n == 3:
    return 2
  if d[n]:
    return d[n]
  d[n] = fibo(n-1)+fibo(n-2)
  
  return d[n]

def solution(n):
    answer = fibo(n) % 1234567
    return answer