cnt = set()
for i in range(10) :
    N = int(input())
    cnt.add(N%42)
print(len(cnt))