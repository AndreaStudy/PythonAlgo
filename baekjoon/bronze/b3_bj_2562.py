import sys

temp = 0
seat = 0
for i in range(1,10):
    N = int(input())
    if temp < N :
        temp = N
        seat = i

print(temp)
print(seat)