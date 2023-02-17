import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    result = -1
    if  N == 1:
        result = 1
    else:
        for i in range(2, N//4):
            if i*i*i == N:
                result = i
                break
            elif i*i*i > N:
                break
    print(f'#{tc} {result}')