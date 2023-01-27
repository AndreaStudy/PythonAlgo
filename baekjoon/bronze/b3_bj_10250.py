T = int(input())

for test_case in range(T) :
    H, W, N = map(int, input().split())
    hosu = (N // H)+1
    floor = N % H
    if floor == 0 :
        floor = H
        hosu -= 1
    print(floor*100+hosu)