import sys; input=sys.stdin.readline

X, Y = map(int,input().split()) 
first = (100*Y) // X 
left = 0 
right = X 
res = X 
if first >= 99 : 
    print(-1)
else: 
    while left <= right: 
        mid = (left + right) // 2 
        if (100 * (Y + mid)) // (X + mid) > first: 
            res = mid 
            right = mid - 1 
        else: 
            left = mid + 1
    print(res)