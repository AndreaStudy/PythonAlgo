T = int(input())
count = 1
n=1
while True :
    if T == 1 :
        break
    T = T-6*n
    count +=1
    n +=1
    if T <= 0 :
        break

print(count)