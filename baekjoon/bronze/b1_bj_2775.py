import sys
input = sys.stdin.readline
T = int(input().rstrip())
sum_list = []
for test_case in range(T) :
    floor = int(input().rstrip())
    ho = int(input().rstrip())
    fl_list = [x for x in range(1, ho+1)]
    for i in range(floor) :
        for j in range(1, ho) :
            fl_list[j] += fl_list[j-1]
    print(fl_list[-1])