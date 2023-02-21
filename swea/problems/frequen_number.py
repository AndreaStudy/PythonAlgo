T = int(input())

for test_case in range(1, T+1) :
    N = int(input())
    scores = list(map(int,input().split()))
    fre_score = [0] * (max(scores) +1)
    mode = 0
    for score in scores :
        fre_score[score] += 1
        if fre_score[score] >= fre_score[mode] :
            mode = score
    print(f'#{test_case} {mode}')