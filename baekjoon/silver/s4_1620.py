import sys
input = sys.stdin.readline

T, N = map(int, input().split())

dogam1 = dict()
dogam2 = dict()
start = 1
for t in range(T):
  poketmon = input().rstrip()
  dogam1[start] = poketmon
  dogam2[poketmon] = start
  start += 1

for n in range(N):
  test = input().rstrip()
  if test.isdigit():
    print(dogam1[int(test)])
  else:
    print(dogam2[test])