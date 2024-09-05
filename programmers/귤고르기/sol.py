from collections import Counter

def solution(k, tangerine):
  answer = 0
  t_cnt = Counter(tangerine)
  s_t_cnt = sorted(t_cnt.items(), key=lambda x: x[1], reverse=True)
  for i in s_t_cnt:
    if k - i[1] <= 0:
      answer += 1
      break
    else:
      k -= i[1]
      answer += 1
    
  return answer