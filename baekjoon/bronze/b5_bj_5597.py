import sys

student = list(range(1,31))
quest = []
for i in range(1,29):
    N = int(sys.stdin.readline().rstrip())
    quest.append(N)
    
for i in student :
    if i in quest :
        continue
    else :
        print(i)