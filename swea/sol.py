T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = input()
    # 받아온 숫자로 2진수로 변환한 후 3번째 값부터 쓸꺼임 1,2번째 값은 0b
    temp = bin(int(nums, 16))[2:]
    cnt = 0
    # 최종 1의 개수가 많은 것을 넣어줄 변수
    result = 0
    # total을 돌면서 값을 확인
    for i in temp:
        # 1일 경우 cnt 추가
        if i == '1':
            cnt += 1
            result = max(result, cnt)
        # 아닐 경우 cnt 초기화
        else:
            cnt = 0
    # 결과 출력
    print(f'#{tc} {result}')