import sys
sys.stdin = open('input.txt')

def elec(n, k):
    global temp, result
    # 최대 깊이
    if k == N:
        # 최대값 갱신
        if temp < result:
            result = temp
        return
    # 마지막에는 무조건 0번 인덱스로 가야함
    if k == N-1:
        temp += arr[n][0]
        elec(0, k+1)
        temp -= arr[n][0]
    # 반복문을 돌며 수행
    for d in range(N):
        # 0인 값은 자기 자신의 위치 이므로 재낌
        if not arr[n][d]:
            continue
        # 방문처리한 곳은 방문 X
        if visited[d]:
            continue
        # 위에 둘다 아니라면 방문처리하고 값을 더해주고
        # 깊이 1을 더한 값을 재귀호출
        # 끝난 뒤는 방문처리를 다시 원래대로하고 값을 다시 빼줌
        else:
            visited[d] = 1
            temp += arr[n][d]
            elec(d, k+1)
            visited[d] = 0
            temp -= arr[n][d]


T = int(input())

for tc in range(1, T+1):
    # N번 관리구역
    N = int(input())
    # 이동시 배터리 소비량
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 0번 인덱스는 1번 관리구역으로 사무실
    visited = [1] + [0] * (N-1)
    temp = 0
    # 최종값을 저장할 변수
    result = 1e10
    # 함수 호출
    elec(0, 0)
    print(f'#{tc} {result}')
