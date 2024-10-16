def solution(want, number, discount):
  answer = 0
  lst = []
  
  for i in range(len(want)):
    for _ in range(number[i]):
      lst.append(want[i])
  lst.sort()
  
  for i in range(len(discount)-9):
    lst_10 = discount[i:i+10]
    lst_10.sort()
    if lst == lst_10:
      answer += 1
      
  return answer