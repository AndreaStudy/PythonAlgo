import sys
sys.stdin = open('input.txt')

def hoare(A, left, right):
    pivot = A[left] # 맨 왼쪽 원소 기준
    i = left # 피봇보다 큰값을 찾아 오른쪽으로 이동
    j = right # 피봇보다 작은 값을 찾아 왼쪽으로 이동
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[j], A[left] = A[left], A[j]
    return j

def quick_sort(A, left, right):
    if left < right:
        start = hoare(A, left, right)
        quick_sort(A, left, start-1)
        quick_sort(A, start+1, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    quick_sort(arr, 0, N-1)
    print(f'#{tc} {arr}')