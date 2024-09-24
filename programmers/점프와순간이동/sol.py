# 순간이동은 쉬프트연산(건전지 X)
# 점프는 1 씩 이동한거라고 생각하면
# 2진법 변환해서 1의 갯수만큼 건전지가 든거임

def solution(n):
  return bin(n).count('1')