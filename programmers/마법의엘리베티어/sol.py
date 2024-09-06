def solution(storey):
    answer = 0
    
    while storey:
        rest = storey % 10
        
        if rest > 5:
            answer += (10-rest)
            storey += 10
        elif rest < 5:
            answer += rest
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += rest
        storey //= 10
                
    return answer