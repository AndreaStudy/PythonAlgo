import sys; input = sys.stdin.readline;

def devide(lst):
  todo = list(lst)
  
  while len(todo) >= 3:
    for i in range(2, len(todo), 2):
      if todo[i-2] == todo[i]:
        return False
      
    next = []
    for i in range(1, len(todo), 2):
      next.append(todo[i])
      
    todo = next
    
  return True


T = int(input())

for _ in range(T):
  str = input().rstrip()
  
  if devide(str):
    print("YES")
  else:
    print("NO")