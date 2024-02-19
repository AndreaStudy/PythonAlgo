import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    answer = 0
    for n in range(N):
        x3, y3, r = map(int, input().split())
        dis1 = (x1-x3)**2 + (y1-y3)**2
        dis2 = (x2-x3)**2 + (y2-y3)**2
        r2 = r**2
        
        if r2 > dis1:
            if r2 > dis2:
                continue
            else:
                answer += 1
        elif r2 > dis2:
            answer += 1
    
    print(answer)
    

