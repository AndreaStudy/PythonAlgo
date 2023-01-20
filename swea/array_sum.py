for _ in range(10) :
    T = int(input())

    arr = [list(map(int,input().split())) for _ in range(100)]

    # 가로, 세로줄, 대각선의 합
    max_1 = 0
    max_2 = 0
    max_3 = 0
    for i in range(100) :
        sum1 = 0
        sum2 = 0
        sum3 = 0
        sum4 = 0
        sum3 += arr[i][i]
        sum4 += arr[-i-1][i]
        if max(sum3, sum4) > max_3 :
            max_3 = max(sum1, sum2)
        for j in range(100) :
            sum1 += arr[i][j]
            sum2 += arr[j][i]
        if sum1 > max_1 :
            max_1 = sum1
        if sum2 > max_2 :
            max_2 = sum2

    result =max(max_1,max_2,max_3)

    print(f'#{T} {result}')