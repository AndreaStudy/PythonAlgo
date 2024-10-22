def solution(sticker):
  n = len(sticker)
  
  # 길이가 1일 경우
  if n == 1:
    return sticker[0]
  # 길이가 2일 경우
  if n == 2:
    return max(sticker)
  
  # 길이가 3이상일 경우
  def max_sum(stickers):
    # dp로 값 저장해서 사용
    dp = [0] * len(stickers)
    dp[0] = stickers[0]
    dp[1] = max(stickers[0], stickers[1])
    
    # 3이상의 경우 dp에 저장
    for i in range(2, len(stickers)):
      # 이전 값과 그 이전의 값 + 현재값 비교해서 더 높은 값을 dp에 저장
      dp[i] = max(dp[i-1], dp[i-2] + stickers[i])
    
    # 제일 마지막 값 리턴
    return dp[-1]
  
  # 마지막 값 제외하고 값 계산
  case1 = max_sum(sticker[:-1])
  # 첫번째 값 제외하고 값 계산
  case2 = max_sum(sticker[1:])
  
  # 둘 중에 큰 값 리턴
  return max(case1, case2)