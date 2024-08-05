import sys; input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
dst = dict()
for i in range(N):
    if dst.get(lst[i]):
        dst[lst[i]] = dst[lst[i]] + 1
    else :
        dst[lst[i]] = 1
M = int(input())
lst2 = list(map(int, input().split()))

for i in range(M):
    if dst.get(lst2[i]):
        print(dst[lst2[i]], end=" ")
    else :
        print(0, end=" ")