from heapq import heappop, heappush

def solution(n, k , enemy):
  if k >= len(enemy):
    return len(enemy)
  
  answer = 0
  num = 0
  hq = []
  
  for e in enemy:
    heappush(hq, -e)
    num += e
    if num > n:
      if not k:
        break
      k -= 1
      num += heappop(hq)
    answer += 1
    
  return answer
  
# 5  
print(solution(7,3,[4,2,4,5,3,3,1]))
