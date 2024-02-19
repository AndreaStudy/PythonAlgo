import sys
from bisect import bisect_left
sys.stdin = open('swea/problems/binarySearch/input.txt')

T = int(input())


def binarySearch(start, end, target):
    global result, flag
    if flag == 3:
        return
    middle = (start+end)//2
    if N_list[middle] == target:
        result += 1
        flag = 3
        return
    if start == end:
        return
    elif N_list[middle] > target:
        if flag in (0, 2):
            flag = 1
            binarySearch(start, middle-1, target)
        flag = 3
    else:
        if flag in (0, 1):
            flag = 2
            binarySearch(middle+1, end, target)
        flag = 3


for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = sorted(list(map(int, input().split())))
    M_list = list(map(int, input().split()))

    result = 0

    for target in M_list:
        flag = 0
        binarySearch(0, N-1, target)

    print(f'#{tc} {result}')
