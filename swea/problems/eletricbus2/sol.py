import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N, *bus_stop_li = map(int, input().split())
    visited = [0] * (N-1)
    for i in range(N-1): # 버스의 충전지를 충전지 + 인덱스로 변환 = 여기서 배터리 주우면 도착하는 위치
        bus_stop_li[i] += i

    max_V = bus_stop_li[0]
    cnt = 0
    while i != (N-1):
        i = max_V
        cnt += 1
        while not visited[i] and i >= 0:
            max_V = max(max_V, bus_stop_li[i])
            if max_V >= N-1:
                i = N-1
                break
            visited[i] = True
            i -= 1

    print(f'#{tc} {cnt}')

# def bus(here, cnt):
#     global result

#     if cnt == result:
#         return
    
#     if here >= N -1:
#         if cnt <= result:
#             result = cnt
#         return
    
#     for i in range(1, station[here]+1):
#         bus(here+i, cnt +1)

# T = int(input())

# for tc in range(1, T+1):
#     station = list(map(int, input().split()))
#     N = station.pop(0)
#     result = 101

#     bus(0, -1)

#     print(f'#{tc} {result}')