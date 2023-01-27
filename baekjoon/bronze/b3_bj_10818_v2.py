import sys
N = int(input())
num_list = list(map(int,sys.stdin.readline().split()))

for i in range(len(num_list)-1) :
    if num_list[i] > num_list[i+1] :
        num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
for i in range(len(num_list)-1) :
    if num_list[-i-1] < num_list[-i-2] :
        num_list[-i-1], num_list[-i-2] = num_list[-i-2], num_list[-i-1]
print(num_list[0], num_list[-1])