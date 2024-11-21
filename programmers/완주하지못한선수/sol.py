def solution(participant, completion):
    p_dic = dict()
    temp = 0
    for p in participant:
        p_dic[hash(p)] = p
        temp += int(hash(p))
    for com in completion:
        temp -= hash(com)
        
    return p_dic[temp]