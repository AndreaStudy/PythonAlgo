def cals(time):
    hours, mins = map(int, time.split(":"))
    return (hours*60+mins)

def solution(fees, records):
    answer = []
    t, c, nt, nc = map(int, fees)
    length = len(records)
    dicRecord = dict()
    for i in range(length):
        time, carNum, record = records[i].split()
        temp = cals(time)
        if record == 'IN':
            if carNum in dicRecord.keys():
                dicRecord[carNum] = (temp, dicRecord[carNum][1])
            else:
                dicRecord[carNum] = (temp, 0)
        else:
            diff = temp - dicRecord[carNum][0]
            dicRecord[carNum] = (1440, dicRecord[carNum][1]+diff)
    
    seq = sorted(dicRecord)
    
    for record in seq:
        if dicRecord[record][0] < 1440:
            temp = cals('23:59')
            dicRecord[record] = (dicRecord[record][0], dicRecord[record][1] + (temp - dicRecord[record][0]))
        if dicRecord[record][1] > t:
            if ((dicRecord[record][1]-t) % nt) > 0:
                answer.append(c+(((dicRecord[record][1]-t)//nt)+1)*nc)
            else:
                answer.append(c+(dicRecord[record][1]-t)//nt*nc)
        else:
            answer.append(c)
            
            
        
    return answer