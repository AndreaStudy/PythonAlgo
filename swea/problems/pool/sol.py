import sys
sys.stdin = open('input.txt')

def dfs(n, sm):
    global ans

    if ans <= sm:
        return

    if n > 12:
        ans = min(ans, sm, year)
        return
    
    dfs(n+1, sm+day*lst[n])
    dfs(n+1, sm+mon)
    dfs(n+3, sm+mon3)

T = int(input())

for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))

    ans = year
    dfs(1, 0)
    print(f'#{tc} {ans}')