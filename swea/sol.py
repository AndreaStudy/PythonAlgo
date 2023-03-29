def quick_sort(array):
    
    if len(array) <= 1:
        return array

    pivot = array[0] 
    tail = array[1:] 

    left_side = [x for x in tail if x <= pivot] 
    right_side = [x for x in tail if x > pivot] 
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

T = int(input())
n = int(input())
arr = list(map(int, input().split()))

result = quick_sort(arr)
print(result)
print(result[n//2])