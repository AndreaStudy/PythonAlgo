import sys
input= sys.stdin.readline

n = int(input().rstrip())
l = []

for _ in range(n):
    l += list(map(int, input().split()))
    l = sorted(l,reverse=True)[:n]

print(l[-1])