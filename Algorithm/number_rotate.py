T = int(input())

for test_case in range(1, T+1):
    # 행렬의 N값
    N  = int(input())
    
    # N x N 행렬
    arr = [list(map(int,input().split())) for _ in range(N)]

    # 90도, 180도, 270도 회전한 행렬 초기화
    arr_90 = [[0 for _ in range(N)] for _ in range(N)]
    arr_180 = [[0 for _ in range(N)] for _ in range(N)]
    arr_270 = [[0 for _ in range(N)] for _ in range(N)]

    # arr 행렬 90도 회전
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]

    # arr_90을 90도 회전하면 180도 회전
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N-1-j][i]

    # arr_180을 90도 회전
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N-1-j][i]

    # 출력
    print(f'#{test_case}')
    for i in range(N) :
        for j in range(N) :
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N) :
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N) :
            print(arr_270[i][j], end='')
        print()