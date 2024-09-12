from heapq import heappop, heappush

def cals(time):
  hours, minutes = map(int,time.split(":"))
  return (hours*60+minutes)

def solution(book_time):
  answer = 1
  
  book_time_ref = [(cals(s), cals(e)) for s, e in book_time]
  book_time_ref.sort()
  
  heap = []
  for s, e in book_time_ref:
    if not heap:
      heappush(heap,e+10)
      continue
    if heap[0] <= s:
      heappop(heap)
    else:
      answer += 1
    heappush(heap,e+10) 
  
  return answer