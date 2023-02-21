T = int(input())

for test_case in range(1, T+1) :
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M :
        N, M = M, N
        A, B = B, A
    max_sum=0
    for i in range(M-N+1) :
        temp =0 
        for j in range(N) :
            temp += A[j] * B[j+i]
        
        if temp > max_sum :
            max_sum = temp
    print(f'#{test_case} {max_sum}')