import sys
import math
input = sys.stdin.readline

A, B, C = map(int,input().split())
if B-C >= 0 :
    print(-1)
else :
    cnt = (math.floor(A/(-(B-C)))+1)
    print(cnt)