import sys
import math
input = sys.stdin.readline

T = int(input())
array = [0] * (10001)
goldbahe = []

for i in range(2, 10001) :
    array[i] = i

for i in range(2, int(math.sqrt(10000))+1) :
    if array[i] == 0 :
        continue
    for j in range(i+i, 10001, i) :
        array[j] = 0

for i in range(2, 10001) :
    if array[i]!=0 :
        goldbahe.append(array[i])
for test_case in range(T) :
    N = int(input())
    n_2 = int(N/2)
    goldbahe_num = []
    if n_2 in goldbahe and n_2*2 == N :
        print(f'{n_2} {n_2}')
    else :
        for i in range(int(len(goldbahe))) :
            if len(goldbahe_num) >0 :
                if goldbahe_num[-1] == goldbahe[i] :
                    break
            for j in range(1, int(len(goldbahe))) :
                if goldbahe[i] + goldbahe[j] < N :
                    continue
                if goldbahe[i] + goldbahe[j] == N :
                    goldbahe_num.append(goldbahe[i])
                    goldbahe_num.append(goldbahe[j])
        if len(goldbahe_num) == 1 :
            print(f'{goldbahe_num[0]} {goldbahe_num[1]}')
        else :
            print(f'{goldbahe_num[-2]} {goldbahe_num[-1]}')