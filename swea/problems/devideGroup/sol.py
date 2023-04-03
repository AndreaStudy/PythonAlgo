import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    visited = [1] + [0] * (N)
    idx = 1
    for i in range(0, M*2, 2):
        if visited[nums[i]]:
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
        print(f'#{tc} {len(result)+sol}')
    else:
        print(f'#{tc} {len(result)-1+sol}')
