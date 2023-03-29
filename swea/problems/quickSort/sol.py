import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0] # 피벗은 첫 번째 원소


    left_side = []
    equal_side = []
    right_side = []
    for i in arr:
        if i < pivot:
            left_side.append(i)
        elif i > pivot:
            right_side.append(i)
        else:
            equal_side.append(i)

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + equal_side + quick_sort(right_side)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {quick_sort(arr)[N//2]}')