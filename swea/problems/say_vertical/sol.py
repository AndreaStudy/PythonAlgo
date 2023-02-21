import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    arr = [list(input().rstrip()) for _ in range(5)]
    
    result = ''
    while arr[0] or arr[1] or arr[2] or arr[3] or arr[4]:
        if arr[0]:
            result += arr[0].pop(0)
        if arr[1]:
            result += arr[1].pop(0)
        if arr[2]:
            result += arr[2].pop(0)
        if arr[3]:
            result += arr[3].pop(0)
        if arr[4]:
            result += arr[4].pop(0)

    print(f'#{tc} {result}')