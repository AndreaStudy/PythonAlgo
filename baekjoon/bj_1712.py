import sys
import math
input = sys.stdin.readline

A, B, C = map(int,input().split())
cnt = (math.floor(A/abs(B-C))+1)
print(cnt)