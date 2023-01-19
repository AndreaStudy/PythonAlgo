import sys
T = int(input())
num_cnt = [0]* 201
num_list = list(map(int,sys.stdin.readline().split()))
for i in num_list :
    num_cnt[i+100] += 1
num = int(input())
print(num_cnt[num+100])