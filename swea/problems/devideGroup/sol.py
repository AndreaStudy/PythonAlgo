import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    visited = [1] + [0] * (N)
    idx = 1
    cnt = 0
    for i in range(0, M*2, 2):
        if visited[nums[i]] and visited[nums[i+1]]:
            if visited[nums[i]] == visited[nums[i+1]]:
                continue
            else:
                cnt += 1
        elif visited[nums[i]]:
            visited[nums[i+1]] = visited[nums[i]]
        elif visited[nums[i+1]]:
            visited[nums[i]] = visited[nums[i+1]]
        else:
            visited[nums[i]] = idx
            visited[nums[i+1]] = idx
            idx += 1
    sol = visited.count(0)
    result = set(visited)
    if sol == 0:
        print(f'#{tc} {len(result)+sol-cnt}')
    else:
        print(f'#{tc} {len(result)-1+sol-cnt}')

# def find(x):
#     if nums[x] == x:
#         return x
#     else:
#         nums[x] = find(nums[x])
#         return find(nums[x])

# def union(x, y):
#     x, y = find(x), find(y)
#     if x != y:
#         nums[y] = x

# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     nums = [i for i in range(N+1)]
#     arr = list(map(int, input().split()))
#     for i in range(0, M*2, 2):
#         union(arr[i], arr[i+1])
#         print(*nums)
#     result = set()
#     for i in range(1, N+1):
#         result.add(find(i))
        
#     print(f'#{tc} {len(result)}')
        
        
        

