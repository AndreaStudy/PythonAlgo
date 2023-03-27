import sys
# sys.stdin = open('input.txt')
T = int(input())

for _ in range(T):
    num = sorted(list(input()))
    cnt = 0
    for a in range(0, 6, 3):
        if num[a] == num[a+1] == num[a+2]:
            cnt += 1
        elif (int(num[a+1]) - int(num[a])) == (int(num[a+2]) - int(num[a+1])) == 1:
            cnt += 1

    if cnt == 2:
        print(True)
    else:
        print(False)

