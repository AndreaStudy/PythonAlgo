def mining(available,mineral,pick) :
    tmp = 0
    for m in mineral :
        tmp += available[m][pick]
    return tmp

def solution(picks, minerals):
  answer = 0
  available = {"diamond": [1,5,25], "iron": [1,1,5], "stone":[1,1,1]}
  dia, iron, stone = picks
  
  minerals = [minerals[i:i+5] for i in range(0,len(minerals),5)] [:sum(picks)]
  minerals.sort(key=lambda x:(x.count("diamond"), x.count("iron"),x.count("stone")),reverse=True)
  
  for mineral in minerals :
    if dia > 0 :
      answer += mining(available,mineral,0)
      dia -= 1
    elif iron > 0 :
      answer += mining(available,mineral,1)
      iron -= 1
    elif stone > 0 :
      answer += mining(available,mineral,2)
      stone -= 1
  return answer


print(solution([1,3,2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))  
