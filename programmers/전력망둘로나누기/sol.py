INF = int(1e9)

def DFS(v, graph, visited, check_link):
    cnt = 1
    visited[v] = 1

    for adj_v in graph[v]:
        if not visited[adj_v] and check_link[v][adj_v]:
            cnt += DFS(adj_v, graph, visited, check_link)

    return cnt


def solution(n, wires):
    answer = INF

    check_link = [[1]*(n+1) for _ in range(n+1)]

    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [0]*(n+1)

        check_link[a][b] = 0
        cnt_a = DFS(a, graph, visited, check_link)
        cnt_b = DFS(b, graph, visited, check_link)
        check_link[a][b] = 1

        answer = min(answer, abs(cnt_a - cnt_b))

    return answer
