def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result

def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    print(f'#{tc} {merge_sort(arr)[N//2]} {cnt}')


# def merge_sort(start, end):
#     global cnt
#     if start == end:
#         return
#     middle = (start+end)//2
#     merge_sort(start, middle)
#     merge_sort(middle+1, end)

#     k = 0
#     left, right = start, middle+1
#     while left <= middle or right <= end:
#         if left <= middle and right <= end:
#             if arr[left] <= arr[right]:
#                 tmp[k] = arr[left]
#                 left += 1
#             else:
#                 tmp[k] = arr[right]
#                 right += 1
#             k += 1
#         elif left <= middle:
#             while left <= middle:
#                 tmp[k] = arr[left]
#                 left += 1
#                 k += 1
#         elif right <= end:
#             while right <= end:
#                 tmp[k] = arr[right]
#                 right += 1
#                 k += 1
#     i = 0
#     while i < k:
#         arr[start + i] = tmp[i]
#         i += 1
#     return


# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     tmp = [0] * N
#     cnt = 0
#     merge_sort(0, N-1)
#     print(f'#{tc} {arr[N//2]} {cnt}')