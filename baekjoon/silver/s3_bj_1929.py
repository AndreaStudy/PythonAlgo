import sys
import math
input = sys.stdin.readline

M, N = map(int, input().split())

array = [0] * (N+1)

for i in range(2, N+1) :
    array[i] = i

for i in range(2, int(math.sqrt(N))+1) :
    if array[i] == 0 :
        continue
    for j in range(i+i, N+1, i) :
        array[j] = 0

for i in range(M, N+1) :
    if array[i]!=0 :
        print(i)


# 시간초과....
# for i in range(M, N+1) :
#     if i == 1 :
#         continue
#     if i == 2 :
#         print(i)
#         continue
#     prime = True
#     for j in range(2, i) :
#         if i  % j == 0 :
#             prime = False
#         if prime == True :
#             print(i)