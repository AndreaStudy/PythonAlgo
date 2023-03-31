import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    s = [0] * 13
    for i in range(1, 13):
        s[i] = s[i-1] + day * lst[i]
        s[i] = min(s[i], s[i-1] + mon)
        if i >= 3:
            s[i] = min(s[i], s[i-3] + mon3)

    ans = min(s[12], year)
    print(f'#{tc} {ans}')