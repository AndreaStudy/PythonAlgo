# 시간초과
# 시간복잡도 고려 X

import sys
input = sys.stdin.readline

N, M  = map(int, input().split())
list_map = [list(map(int, input().split())) for _ in range(N)]

for i in range(M) :
    map_point = list(map(int, input().split()))
    x1, y1, x2, y2 = map_point[0], map_point[1], map_point[2], map_point[3]
    if x1 == x2 and y1 == y2 :
        print(list_map[x1][y1])
    else :
        sum = 0
        while True :
            sum += list_map[x1-1][y1-1]
            if x1 == x2 and y1 == y2 : break
            if y1 == y2 :
                y1 = map_point[1]
                x1 +=1
                continue
            y1 +=1
        print(sum)