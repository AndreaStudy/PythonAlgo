# 누적합구하는 공식
# table[x2][y2] - table[x2][y1-1] - table[x1-1][y2] + table[x1-1][y1-1]
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
table = []
sum_table = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    table.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_table[i][j] = sum_table[i][j-1] + table[i-1][j-1]
for i in range(1, n+1):
    for j in range(1, n+1):
        sum_table[i][j] = sum_table[i-1][j] + sum_table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = sum_table[x2][y2] - sum_table[x2][y1 - 1] - sum_table[x1 - 1][y2] + sum_table[x1-1][y1-1]
    print(answer)