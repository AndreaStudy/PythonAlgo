def solution(numbers):
    answer = []
    length = len(numbers)
    
    maxi = max(numbers)
    
    for i in range(length):
        if numbers[i] == maxi:
            answer.append(-1)
            continue;
        for j in range(i+1, length):
            if numbers[i] < numbers[j]:
                answer.append(numbers[j])
                break;
            elif j == length-1:
                answer.append(-1)
                
        if i == length-1:
            answer.append(-1)
    
    return answer