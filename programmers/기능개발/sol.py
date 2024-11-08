def solution(progresses, speeds):
    qList = []
    
    for p, s in zip(progresses, speeds):
        if len(qList) == 0 or qList[-1][0] < -((p-100)//s):
            qList.append([-((p-100)//s),1])
        else:
            qList[-1][1] += 1
    
    return [q[1] for q in qList]