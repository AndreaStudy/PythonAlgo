from collections import deque

def solution(elements):
  answer = set()
  q = deque(elements)
  for i in range(len(elements)):
    sum = 0
    for e in q:
      sum += e
      answer.add(sum)
      
    q.append(q.popleft())
    
  return len(answer)

# def solution2(elements):
#   answer = set()
#   length = len(elements)
#   for i in range(1, length+1):
#     for j in range(length):
#       sum = 0
#       for k in range(j, j+i):
#         sum += elements[k%length]
#       answer.add(sum)
      
#   return len(answer)