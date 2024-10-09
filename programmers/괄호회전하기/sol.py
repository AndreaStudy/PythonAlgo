def check(s):
  stack = []
  for i in s:
    if not stack:
      stack.append(i)
    elif i == ')':
      if stack[-1] == '(':
        stack.pop()
      else:
        return False
    elif i == '}':
      if stack[-1] == '{':
        stack.pop()
      else:
        return False
    elif i == ']':
      if stack[-1] == '[':
        stack.pop()
      else:
        return False
    else:
      stack.append(i)
  if stack:
    return False
  return True

def solution(s):
  if len(s) % 2:
    return 0
  answer = 0
  for i in range(len(s)):
    temp = s[i:] + s[:i]
    if check(temp):
      answer += 1
  
  return answer