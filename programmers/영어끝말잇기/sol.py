def solution(n, words):
  answer = [0,0]
  lst = [words[0]]
  for i in range(1, len(words)):
    if words[i] in lst or lst[-1][-1] != words[i][0]:
      answer[0] = i%n+1
      answer[1] = i//n+1
      break
    else:
      lst.append(words[i])

  return answer