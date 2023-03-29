import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    def sort(left, right):
        if right - left < 2:
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        merge(left, mid, right)

    def merge(left, mid, right):
        temp = []
        l, h = left, mid

        while l < mid and h < right:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < right:
            temp.append(arr[h])
            h += 1

        for i in range(left, right):
            arr[i] = temp[i - left]

    return sort(0, len(arr))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    merge_sort(arr)
    print(f'#{tc} {arr[N//2]}')