import sys; input=sys.stdin.readline;

def gcd(a,b):
  while b > 0:
    tmp = a%b
    a = b
    b = tmp
  return a

def multiply(lst):
  return eval('*'.join([str(n) for n in lst]))

N = int(input())
nlst = list(map(int, input().split()))
M = int(input())
mlst = list(map(int, input().split()))

a = multiply(nlst)
b = multiply(mlst)

print('%s'%str(gcd(a,b))[-9:])