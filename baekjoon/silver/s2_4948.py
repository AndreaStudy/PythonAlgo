import sys
import math
input = sys.stdin.readline

array = [0,0] + [1]*(123456*2+1)

for i in range(2, int(math.sqrt(len(array))+1)) :
    if array[i] :
        j=2
        while i * j <= 2*123456:
            array[i*j] = 0
            j +=1

while True :
    N = int(input())
    if N == 0 :
        break
    print(sum(array[N+1:2*N+1]))


# def prime(num) :
#     cnt = 0
#     for i in range(num+1, 2*num) :
#         cnt +=1
#         for j in range(2, int(math.sqrt(i))+1) :
#             if i % j == 0 :
#                 cnt -=1
#                 break

#     return cnt

# while True :
#     N = int(input().rstrip())
#     if N == 0 :
#         break
#     elif N == 1 :
#         print(1)
#     else :
#         print(prime(N))