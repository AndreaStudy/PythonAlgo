import sys
sys.stdin = open('input.txt')

def bus(here, cnt):
    global result

    if cnt == result:
        return
    
    if here >= N -1:
        if cnt <= result:
            result = cnt
        return
    
    for i in range(1, station[here]+1):
        bus(here+i, cnt +1)

T = int(input())

for tc in range(1, T+1):
    station = list(map(int, input().split()))
    N = station.pop(0)
    result = 101

    bus(0, -1)

    print(f'#{tc} {result}')