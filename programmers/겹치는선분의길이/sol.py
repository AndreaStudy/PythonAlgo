def solution(lines):
  lst = [0] * 200
  for start, end in lines:
    for i in range(start, end):
      lst[i+100] += 1
  
  answer = 0
  for l in lst:
    if l >= 2:
      answer += 1
  
  return answer