h, m = map(int, input().split())
time = int(input())
nm = m+time

while nm >= 60 :
    nm -= 60
    h += 1
    if h > 23 :
        h=0
print(h, nm)