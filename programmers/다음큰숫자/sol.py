def cals(n):
  binN = bin(n)[2:]
  cnt = 0
  for i in binN:
    if i == '1':
      cnt += 1
  return cnt

def solution(n):
    answer = 0
    cnt = cals(n)
    while True:
      n += 1
      if cals(n) == cnt:
        answer = n
        break
    return answer
  
print(solution(15))