import sys
input = sys.stdin.readline

def rightrotate(n):
    if n == 4:
        return
    if cycle[n-1][2] != cycle[n][6]:
        temp[n-1] = temp[n] = 1
        rightrotate(n+1)
    return

def leftrotate(n):
    if n == 1:
        return
    if cycle[n-1][6] != cycle[n-2][2]:
        temp[n-1] = temp[n-2] = 1
        leftrotate(n-1)
    return

def cal(d):
    for i in range(4):
        if temp[i]:
            if i in (0,2):
                if d == 1:
                    tmp = [cycle[i].pop()]
                    cycle[i] = tmp + cycle[i]
                    print('1')
                else:
                    tmp = [cycle[i][0]]
                    cycle[i] = cycle[i][1:]+tmp
                    print('2')
            else:
                if d == 1:
                    tmp = [cycle[i][0]]
                    cycle[i] = cycle[i][1:]+tmp
                    print('3')
                else:
                    tmp = [cycle[i].pop()]
                    cycle[i] = tmp + cycle[i]
                    print('4')
                
cycle = [list(input().rstrip()) for _ in range(4)]
K = int(input())
for _ in range(K):
    temp = [0, 0, 0, 0]
    N, dir = map(int, input().split())
    rightrotate(N)
    leftrotate(N)
    cal(dir)
    for i in cycle:
        print(*i)
    

# 계산
result = 0
if cycle[0][0] == '1':
    result += 1
if cycle[1][0] == '1':
    result += 2
if cycle[2][0] == '1':
    result += 4
if cycle[3][0] == '1':
    result += 8
    
print(result)
