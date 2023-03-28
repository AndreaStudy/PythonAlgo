import sys
sys.stdin = open('input.txt')

def change(numbers, cnt):
    # 전역변수 선언
    global result

    # 현재 값
    info = ''.join(numbers)
    
    # 현재 값이 현재 깊이의 리스트 값에 있으면 return
    if int(info) in result[cnt]:
        return
    # 없으면 추가
    else:
        result[cnt].append(int(info))
    # 깊이가 0일 경우 return
    if cnt == 0:
        return

    # 재귀호출
    for i in range(length):
        for j in range(i+1, length):
            # 값 바꿔주기
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 재귀호출 깊이 -1
            change(numbers, cnt-1)
            # 값 원상복귀
            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())

for tc in range(1, T+1):
    # 숫자판, 교환횟수 입력
    info, cnt = input().split()
    # 리스트
    numbers = list(info)
    # 길이 입력
    length = len(numbers)
    # 깊이별로 나오는 값을 저장할 2차원 리스트
    result = [[] for _ in range(int(cnt)+1)]

    # 함수호출
    change(numbers, int(cnt))

    print(f'#{tc} {max(result[0])}')