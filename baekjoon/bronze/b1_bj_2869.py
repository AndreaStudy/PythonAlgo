A,B,V = map(int,input().split())
day = (V-B)/(A-B)
if day != int(day) :
    day +=1
print(int(day))