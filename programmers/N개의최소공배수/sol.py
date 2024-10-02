# 유클리드 호제법 두수의 최대공약수는 a>b일떄 a를 b로 나눈 나머지가 r일때 a와 b의 최대 공약수는 b와 r의 최대공약수와 같다.
def gcd(a, b):
  while b:
    r = a % b
    a, b = b, r
  return a

# 최소공배수는 두수의 곱에서 최대공약수를 나눈 값이다.
def lcm(a,b):
  return a*b // gcd(a,b)

def solution(arr):
    n = arr[0]
    for i in arr[1:]:
      n = lcm(n, i)
    return n