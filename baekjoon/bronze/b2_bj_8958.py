T =  int(input())

for test_case in range(T) :
    count = 1
    total = 0
    for correct in input() :
        if correct == 'O' :
            total += count
            count += 1
        else :
            count =1
    print(total)