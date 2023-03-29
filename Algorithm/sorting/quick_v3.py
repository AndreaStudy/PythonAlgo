def quick_sort(arr, left, right):
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid -1)
        quick_sort(arr, mid+1, right)

def cal(arr, left, right):
    i = left -1
    j = left
    pivot = arr[right]
    while j < right:
        if pivot > arr[j]:
            i += 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1

nums = [11,45,23,81,28,34]
quick_sort(nums, 0,  len(nums)-1)
print(nums)
