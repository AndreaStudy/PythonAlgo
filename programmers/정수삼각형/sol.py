def solution(triangle):
    length = len(triangle)
    
    for i in range(1, length):
        for j in range(i + 1):
            if j == 0:
                # 첫 번째 열
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                # 마지막 열
                triangle[i][j] += triangle[i-1][j-1]
            else:
                # 중간 열
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    return max(triangle[-1])
