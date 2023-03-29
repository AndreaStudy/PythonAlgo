def merge_sort(start, end):
    global cnt
    if start == end:
        return
    middle = (start+end)//2
    merge_sort(start, middle)
    merge_sort(middle+1, end)

    k = 0
    left, right = start, middle+1
    if arr[middle] > arr[end]:
        print(arr[middle], arr[end])
        cnt += 1
    while left <= middle or right <= end:
        if left <= middle and right <= end:
            if arr[left] <= arr[right]:
                tmp[k] = arr[left]
                left += 1
            else:
                tmp[k] = arr[right]
                right += 1
            k += 1
        elif left <= middle:
            while left <= middle:
                tmp[k] = arr[left]
                left += 1
                k += 1
        elif right <= end:
            while right <= end:
                tmp[k] = arr[right]
                right += 1
                k += 1
    i = 0
    while i < k:
        arr[start + i] = tmp[i]
        i += 1
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0
    merge_sort(0, N-1)
    print(f'#{tc} {arr[N//2]} {cnt}')