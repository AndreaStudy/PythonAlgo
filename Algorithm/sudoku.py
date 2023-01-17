T = int(input())
answer = []
size = 9
 
for n in range(T):
    arr = []
    correct = True
 
    for i in range(size):
        temp = list(map(int, input().split()))
        arr.append(temp)
 
    for i in range(size):
        temp = arr[i]
        if (len(set(temp)) != size):
            correct = False
            break
 
    if not correct:
        answer.append(0)
        continue
 
    for i in range(size):
        temp = [row[i] for row in arr]
 
        if (len(set(temp)) != size):
            correct = False
            break
    if not correct:
        answer.append(0)
        continue
 
    for center_i in range(1, size + 1, 3):
        for center_j in range(1, size + 1, 3):
 
            temp = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    temp.append(arr[center_i + i][center_j + j])
 
            if (len(set(temp)) != size):
                correct = False
                break
    if not correct:
        answer.append(0)
        continue
 
    answer.append(1)
 
 
for i in range(T):
    print(f"#{i+1} {answer[i]}")