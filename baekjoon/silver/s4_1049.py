import sys; input=sys.stdin.readline

N, M = map(int, input().split())
a, b = N // 6, N % 6
Gmin, Smin = 1000, 1000

for i in range(M):
    Gcost, Scost = map(int, input().split())
    Gmin, Smin = min(Gmin, Gcost), min(Smin, Scost)

if Gmin > 6*Smin:
    print(N*Smin)
else :
    if (Gmin < b*Smin):
        print((a+1)*Gmin)
    else :
        print(a*Gmin +b*Smin)