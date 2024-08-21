import sys; input = sys.stdin.readline

def pleasuer(l, j, i):
  global joy
  if i == n:
    if joy < j:
      joy = j
    return
  pleasuer (l, j, i+1)
  if l - L[i] > 0:
    pleasuer(l - L[i], j + J[i], i+1)
    
n = int(input())

L = list(map(int, input().split()))
J = list(map(int, input().split()))

l, j = 100, 0

joy =0
pleasuer(l, j, 0)

print(joy)