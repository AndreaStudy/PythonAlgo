import sys
input = sys.stdin.readline

def rotate(n, d):
    if cycle[0][2] != cycle[1][6]:
        temp[0] = temp[1] = 1
    if cycle[1][2] != cycle[2][6]:
        temp[1] = temp[2] = 1
    if cycle[2][2] != cycle[3][6]:
        temp[2] = temp[3] = 1
    for i in range(4):
        if temp[i]:
            if n in (1,3):
                if d == 1:
                    tmp = [cycle[n-1].pop()]
                    cycle[n-1] = tmp + cycle[n-1]
                else:
                    tmp = [cycle[n-1][0]]
                    cycle[n-1] = cycle[n-1][1:]+tmp
            else:
                if d == 1:
                    tmp = [cycle[n-1][0]]
                    cycle[n-1] = cycle[n-1][1:]+tmp
                else:
                    tmp = [cycle[n-1].pop()]
                    cycle[n-1] = tmp + cycle[n-1]
                
cycle = [list(map(int, input().split())) for _ in range(4)]
K = int(input())
for _ in range(K):
    temp = [0, 0, 0, 0]
    N, dir = map(int, input().split())
    rotate(N, dir)
    

# 계산




# 1번의 2번인덱스와 2번의 6번 인덱스
# 2번의 2번인덱스와 3번의 6번 인덱스
# 3번의 2번인덱스와 4번의 6번 인덱스

# 2번이 돌아갈때  모든 인덱스를 체크 하여 돌아가는지 확인
# 돌아가는 바퀴와 인덱스 확인 후 돌리기
# n = 1, d= 1,-1 일때
# 시계, 반시계, 시계, 반시계
# 반시계, 시계, 반시계, 시계
# n = 2, d= 1, -1
# 반시계, 시계, 반시계, 시계
# ....
