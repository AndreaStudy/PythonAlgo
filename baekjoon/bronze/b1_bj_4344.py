import sys
T = int(input())

for test_case in range(T) :
    scores = list(map(int, sys.stdin.readline().split()))
    avg = (sum(scores)-scores[0])/scores[0]
    count = 0
    for avg_over in scores[1:] :
        if avg_over > avg :
            count += 1
    print(f'{(count*100/scores[0]):.3f}%')
