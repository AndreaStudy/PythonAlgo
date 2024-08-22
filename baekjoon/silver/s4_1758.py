import sys; input = sys.stdin.readline

N = int(input())
lst = []

for i in range(N):
  lst.append(int(input()))

lst.sort(reverse=True)
result = 0

for i in range(N):
  tip = lst[i]-(i)
  if tip > 0:
    result += tip
    
print(result)