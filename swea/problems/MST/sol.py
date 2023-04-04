import sys
sys.stdin = open('input.txt')

def find_set(x): # x가 속한 집합의 대표 리턴
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y): # y의 대표원소가 x의 대표원소를 가리키도록
    rep[find_set(y)] = find_set(x)

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    rep = [i for i in range(V+1)]
    arr = [list(map(int, input().split())) for _ in range(E)]
    arr.sort(key = lambda x : x[2])
    cnt = 0
    s = 0
    for u, v, w in arr:
        if find_set(u) != find_set(v):
            cnt += 1
            s += w
            union(u, v)
            if cnt == V:
                break
            
    print(f'#{tc}', s)