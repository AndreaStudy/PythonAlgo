from itertools import permutations

def find(num):
  if num < 2:
    return False
  for i in range(2, int(num**0.5) +1):
    if not num % i:
        return False
  return True

def solution(numbers):
  answer = []
  nums = list(map(str, numbers))
  per = []
  for i in range(1, len(numbers)+1):
    per += [int(("").join(l)) for l in list(permutations(nums, i))]
  
  for n in set(per):
    if find(n):
      answer.append(n)
  
  return len(answer)