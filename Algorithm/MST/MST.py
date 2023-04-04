def find_set(x): # x가 속한 집합의 대표 리턴
    while x != rep[x]:
        x = rep[x]
    return x

def union(x, y): # y의 대표원소가 x의 대표원소를 가리키도록
    rep[find_set(y)] = find_set(x)

V, E = map(int, input().split())

rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    v1, v2, w = map(int, input().split())
    graph.append([v1, v2, w])
    
graph.sort(key = lambda x : x[2])

N = V + 1
s = 0
cnt = 0
MST = []
for u, v, w in graph: # 가중치가 작은 것 부터
    if find_set(u) != find_set(v):
        cnt += 1
        s += w
        MST.append([u, v, w])
        union(u, v)
        if cnt == N-1:
            break
print(s)
print(*MST)