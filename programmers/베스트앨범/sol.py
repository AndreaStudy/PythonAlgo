def solution(genres, plays):
  answer = []
  total = dict()
  gen = dict()
  
  for i in range(len(genres)):
    # 장르별 전체 재생된 횟수
    total[genres[i]] = total.get(genres[i], 0) + plays[i]
    # 장르별 개별 재생된 횟수 + 인덱스
    gen[genres[i]] = gen.get(genres[i], []) + [(plays[i], i)]
      
  # 총 재생된 횟수를 내림차순으로 정렬
  sortedGen = sorted(total.items(), key=lambda x:x[1], reverse=True)
  
  # 내림차순 정렬된 순서대로
  for (genre, totalPlay) in sortedGen:
    # 장르별 개별 항목을 재생순으로 내림차순하고, 같을 경우 인덱스값으로 오름차순정렬
    gen[genre] = sorted(gen[genre], key=lambda x: (-x[0], x[1]))
    # 해당 정렬된 순서에서 상위 2개만 추가
    answer += [i for (play, i) in gen[genre][:2]]
  
  return answer