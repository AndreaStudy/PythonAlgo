import sys

T = int(input())
total = 0
subject = list(map(int, sys.stdin.readline().split()))
highSub = max(subject)

for i in subject :
    total += i/highSub * 100

print(total/T)