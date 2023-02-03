import heapq
import sys
sys.stdin = open("input.txt")
################################################
t = int(input())

INF = int(10e9)
for test_cast in range(1, t+1):
    k, n, m = map(int, input().split())

    charge = [0] + list(map(int, input().split()))

    dis = [INF for _ in range(n+1)]
    dis[0] = 0

    bus_station = [[] for _ in range(n + 1)]

    # 각 충전소에서 다른 충전소로 갈수있는 위치를 저장
    for i in range(m + 1):
        for j in range(i+1, m + 1):
            if charge[j] > charge[i] + k:
                break

            bus_station[charge[i]].append(charge[j])

    # 도착지까지 갈수잇는 정류소 저장
    for i in range(n-k, n+1):
        bus_station[i].append(n)

    # 방문해야 하는 정류장 힙
    visit = []
    # 시작지점 cost와 dis로 저장
    heapq.heappush(visit, [0, 0])

    # 다익스트라 탐색
    while visit:
        cost, charge_spot = heapq.heappop(visit)

        for next_spot in bus_station[charge_spot]:

            if dis[next_spot] > cost + 1:
                dis[next_spot] = cost + 1
                heapq.heappush(visit, [cost+1, next_spot])

    # 도착 불가능 할시 0 출력
    if dis[n] == INF:
        print(f"#{test_cast} 0")

    else:
        # 마지막 도착 이동은 충전 x
        print(f"#{test_cast} {dis[n]-1}")