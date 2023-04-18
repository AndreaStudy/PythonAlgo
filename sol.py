import sys
input = sys.stdin.readline

INF = 1e9

N = int(input())
M = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
result = [[""] * (N+1) for _ in range(N+1)]

for m in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
        result[a][b] = str(a)

for a in range(1, N+1):
    graph[a][a] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                result[i][j] = result[i][k] + ' ' + result[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        print(graph[i][j], end=' ')
    print()
                
for i in range(1, N+1):
    for j in range(1, N+1):
        if result[i][j] != '':
            result[i][j] = result[i][j] + ' ' + str(j)
            print(str(len(result[i][j])//2+1)+ ' ' + result[i][j])
        else:
            print(0)

    

