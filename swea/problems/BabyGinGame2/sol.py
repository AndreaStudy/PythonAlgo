import sys
sys.stdin = open('input.txt')

T = int(input())

def babygin(num, arr):  # 카드숫자, 카운팅리스트
    arr[num] += 1
    flag = 0
    i = 0
    while i < 10:
        if arr[i] >= 3:  # triplet check
            flag = 1
            break
        if arr[i] and arr[i + 1] and arr[i + 2]:  # run check
            flag = 1
            break
        i += 1
    if flag == 1:
        return True


for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    player1, player2 = [0]*12, [0]*12

    winner = 0
    for i in range(0, len(numbers), 2):
        if babygin(numbers[i], player1):
            winner = 1
            break
        if babygin(numbers[i+1], player2):
            winner = 2
            break

    print(f'#{tc} {winner}')

# def check(player):
#     for i in range(len(player)-2):
#         if player[i] == player[i+1] == player[i+2]:
#             return 1
#         if (player[i+1]-player[i]) == (player[i+2]-player[i+1]) == 1:
#             return True
#     return False

# T = int(input())

# for tc in range(1, T+1):
#     numbers = list(map(int, input().split()))

#     player1 = []
#     player2 = []
#     result = 0

#     for i in range(0, len(numbers), 2):
#         player1.append(numbers[i])
#         player2.append(numbers[i+1])
#         if i >= 4:
#             player1.sort()
#             if check(player1):
#                 result = 1
#                 break
#             player2.sort()
#             if check(player2):
#                 result = 2
#                 break

#     print(f'#{tc} {result}')
        