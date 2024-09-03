def solution(numbers):
  length = len(numbers)
  answer = [0] * length
  stack = [0]
  
  for i in range(1, length):
    while stack and numbers[stack[-1]] < numbers[i]:
      answer[stack.pop()] = numbers[i]
    stack.append(i)
    
  while stack:
    answer[stack.pop()] = -1
    
  return answer